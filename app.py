from flask import Flask, render_template, request, redirect, url_for, session, jsonify, abort, g, send_file
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from io import BytesIO
from datetime import datetime, timedelta
import pandas as pd
from threading import Thread
import os, signal, atexit

from auth import authLog
from config import sqliteConfig
from modules import main, tableConfig
from siemens import plc, hmi, scada

app = Flask(__name__)
app.secret_key = '4f3d6e9a5f4b1c8d7e6a2b3c9d0e8f1a5b7c2d4e6f9a1b3c8d0e6f2a9b1d3c4'

@app.route('/')
@app.route('/home')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard', user=session['username'], role=session.get('role')))
    else:
        return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    return render_template('home.html')

@app.route('/logs')
def logs():
    return render_template('logs.html')

@app.route('/generate')
def generate():
    df = main.tbl_fun_View()
    function_list = df[['Id', 'FunctionName']].to_dict(orient='records')
    return render_template('generate.html', function_list=function_list)

@app.route('/generate/fb', methods=['POST'])
def generate_fb():
    data = request.get_json()
    nr = data.get("plc_nr")
    selection_module = data.get("selection_module")
    df_data = data.get("df_data")

    if not nr or not selection_module:
        return jsonify({"status": "error", "message": "PLC number or module name is missing."}), 400

    if not isinstance(df_data, dict) or selection_module not in df_data:
        return jsonify({"status": "error", "message": f"'{selection_module}' sheet not found in Excel."}), 400

    try:
        df = pd.DataFrame(df_data[selection_module])
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error loading sheet: {str(e)}"}), 500

    file_path = plc._exportLogixRungsSie(nr, selection_module, df)
    
    if not file_path or not os.path.exists(file_path):
        return jsonify({"status": "error", "message": "File generation failed."}), 500

    return send_file(file_path, as_attachment=True, download_name=os.path.basename(file_path))


@app.route('/generate/db', methods=['POST'])
def generate_db():
    data = request.get_json()
    nr = data.get("plc_nr")
    selection_module = data.get("selection_module")
    df_data = data.get("df_data")
    cmd_optimized_db = data.get("cmd_optimized_db", False)

    if not nr or not selection_module:
        return jsonify({"status": "error", "message": "PLC number or module name is missing."}), 400

    if not isinstance(df_data, dict) or selection_module not in df_data:
        return jsonify({"status": "error", "message": f"'{selection_module}' sheet not found in Excel."}), 400

    try:
        df = pd.DataFrame(df_data[selection_module])
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error converting sheet to DataFrame: {str(e)}"}), 500

    file_info = plc._exportTiaDbSie(nr, selection_module, df, cmd_optimized_db)
    print("done")
    print(file_info, type(file_info))
    # If file_info is dict, extract path
    if isinstance(file_info, dict):
        file_path = file_info.get("filepath") or file_info.get("file_path") or file_info.get("filename")
    else:
        file_path = file_info

    if not file_path or not os.path.exists(file_path):
        return jsonify({"status": "error", "message": "File generation failed."}), 500
    print("Done")
    return send_file(file_path, as_attachment=True, download_name=os.path.basename(file_path))

@app.route('/generate/textlist', methods=['POST'])
def generate_textlist():
    data = request.get_json()
    nr = data.get("plc_nr")
    selection_module = data.get("selection_module")
    df_data = data.get("df_data")

    if not nr or not selection_module:
        return jsonify({"status": "error", "message": "PLC number or module name is missing."}), 400

    if not isinstance(df_data, dict) or selection_module not in df_data:
        return jsonify({"status": "error", "message": f"'{selection_module}' sheet not found in Excel."}), 400

    try:
        df = pd.DataFrame(df_data[selection_module])
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error converting sheet to DataFrame: {str(e)}"}), 500
    
    file_result = plc._exportPlcTextlistSie(nr, selection_module, df)

    # 🔍 Check if an error dictionary was returned
    if isinstance(file_result, dict) and file_result.get("status") == "error":
        return jsonify(file_result), 500

    file_path = file_result  # This is a string if successful

    if not isinstance(file_path, str) or not os.path.exists(file_path):
        return jsonify({"status": "error", "message": "File generation failed."}), 500

    return send_file(file_path, as_attachment=True, download_name=os.path.basename(file_path))

@app.route('/configuration')
def configuration():
    return redirect(url_for('configuration_tab', tab='view'))

@app.route('/configuration/<tab>')
def configuration_tab(tab):
    user_logged_in = 'username' in session
    df_table1 = main.tbl_fun_View()
    function_list = df_table1[['Id', 'FunctionName']].to_dict(orient='records')
    df_table1 = df_table1.to_html(classes='table table-striped', index=False, escape=False, table_id='inventory-table')

    df_table2 = main.relative_tbl_data()

    if 'FunctionId' in df_table2.columns:
        df_table2 = df_table2.drop(columns=['FunctionId'])

    df_table2 = df_table2.to_html(classes='table table-striped', index=False, escape=False, table_id='inventory-table')

    if tab == 'add':
        return render_template('addtabledata.html', table2=df_table2, function_list=function_list, tab='add', user_logged_in=user_logged_in)
    return render_template('viewtable.html', table1=df_table1, tab='view', user_logged_in=user_logged_in)

@app.route('/configuration/add/<function_id>')
def get_function_data(function_id):
    df_data = main.relative_tbl_data()
    df_data.columns = [col.strip() for col in df_data.columns]

    if function_id != "all":
        try:
            function_id = int(function_id)
            df_data = df_data[df_data['FunctionId'] == function_id]
        except ValueError:
            return jsonify({'html': '<p>Error: Invalid Function ID</p>'})

    if 'FunctionId' in df_data.columns:
        df_data = df_data.drop(columns=['FunctionId'])

    html = df_data.to_html(classes='table table-striped', index=False, escape=False, table_id='inventory-table')
    return jsonify({'html': html})


@app.route('/update_function_view_row', methods=['POST'])
def update_function_view_row():
    if 'username' not in session:
        return jsonify(success=False, error="Not logged in"), 403
    
    data = request.get_json()
    id = data.get('id')
    fun = data.get('function_name')
    fundec = data.get('function_description')
    
    if not id or fun is None or fundec is None:
        return jsonify(success=False, error="Missing data")

    success = tableConfig.edit_fun_tbl(id, fun, fundec)
    return jsonify(success=success)
    
@app.route('/delete_function_view_row', methods=['POST'])
def delete_function_view_row():
    data = request.get_json()
    id = data.get('id')

    if not id:
        return jsonify(success=False, error="ID not provided")

    success =  tableConfig.delete_fun_tbl(id)
    return jsonify(success=success)

@app.route('/add_function_view_row', methods=['POST'])
def add_function_view_row():
    data = request.get_json()
    fun = data.get('function_name')
    fundec = data.get('function_description')

    if not fun or not fundec:
        return jsonify(success=False, error="Missing data")

    success = tableConfig.insert_fun_tbl(fun, fundec)
    return jsonify(success=success)

@app.route('/update_function_adddata_row', methods=['POST'])
def update_function_adddata_row():
    if 'username' not in session:
        return jsonify(success=False, error="Not logged in"), 403
    
    data = request.get_json()
    id = data.get('id')
    function_id = data.get('function_id')
    object = data.get('function_object')
    defValue = data.get('function_default_value')
    worksheetName = data.get('function_worksheet_name')
    
    if not id or object is None or defValue is None or worksheetName is None:
        return jsonify(success=False, error="Missing data")

    success = tableConfig.edit_fundata_tbl(id, function_id, object, defValue, worksheetName)
    return jsonify(success=success)
    

@app.route('/delete_function_adddata_row', methods=['POST'])
def delete_function_adddata_row():
    data = request.get_json()
    id = data.get('id')

    if not id:
        return jsonify(success=False, error="No such ID is available")

    success =  tableConfig.delete_fundata_tbl(id)
    return jsonify(success=success)

@app.route('/add_function_adddata_row', methods=['POST'])
def add_function_adddata_row():
    data = request.get_json()
    function_id = data.get('function_id')
    object = data.get('objects_name')
    defValue = data.get('default_value')
    worksheetName = data.get('worksheet_name')

    if not object or not defValue or not worksheetName or not function_id:
        return jsonify(success=False, error="Missing data")

    success = tableConfig.insert_fundata_tbl(function_id, object, defValue, worksheetName)
    return jsonify(success=success)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/super_admin')
def super_admin():
    user_logged_in = 'username' in session
    df = sqliteConfig.dfUser()
    table_html = df.to_html(classes='table table-striped', index=False, escape=False, table_id='inventory-table')
    return render_template('super_admin.html', table=table_html, user_logged_in=user_logged_in)

@app.route('/update_user_password', methods=['POST'])
def update_user_password():
    data = request.get_json()
    username = data.get('username')
    new_password = data.get('new_password')

    if not username or not new_password:
        return jsonify(success=False, error="Invalid data")

    try:
        conn = sqliteConfig.get_db_connection()
        cur = conn.cursor()
        hashed = generate_password_hash(new_password)

        cur.execute("UPDATE users SET password_hash = ? WHERE username = ?", (hashed, username))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify(success=True)
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = authLog.get_user(username)
    if user and check_password_hash(user[2], password):
        session.permanent = True
        session['username'] = user[1]
        session['role'] = user[3]
        return jsonify(success=True)
    else:
        return jsonify(success=False, error="Invalid Credentials"), 403

@app.route('/change_password', methods=['POST'])
def change_password():
    if 'username' not in session:
        return jsonify(success=False, error="Not logged in"), 403

    data = request.get_json()
    old_password = data.get('oldPassword')
    new_password = data.get('newPassword')

    username = session['username']

    conn = sqliteConfig.get_db_connection()
    if conn is None:
        return jsonify(success=False, error="Database connection error"), 500

    try:
        cur = conn.cursor()
        # Fetch the stored password hash
        cur.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
        row = cur.fetchone()

        if not row:
            return jsonify(success=False, error="User not found"), 404

        stored_password_hash = row[0]

        if check_password_hash(stored_password_hash, old_password):
            # If old password matches, update with new password
            new_password_hash = generate_password_hash(new_password)

            cur.execute('UPDATE users SET password_hash = ? WHERE username = ?', (new_password_hash, username))
            conn.commit()

            return jsonify(success=True)
        else:
            return jsonify(success=False, error="Old password is incorrect."), 400

    except Exception as e:
        print("Error during password change:", e)
        return jsonify(success=False, error=str(e)), 500

    finally:
        cur.close()
        conn.close()

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

@app.before_request
def load_user():
    g.user = session.get('username')
    g.role = session.get('role')

@app.context_processor
def inject_user():
    return dict(user=session.get('username'), role=session.get('role'))
    
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)