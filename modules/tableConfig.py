import pandas as pd

from config import sqliteConfig

def edit_fun_tbl(id, fun, fundec):
    # Get connections and cursors from your SQLite config
    cursorRead, cursorWrite, engineConRead, engineConWrite, conn = sqliteConfig.sqlite()
    
    try:
        update_query = """
            UPDATE Functions 
            SET FunctionName = ?, FunctionDescription = ? 
            WHERE Id = ?
        """
        cursorWrite.execute(update_query, (fun, fundec, id))
        conn.commit()
        return True  # Update successful
    except Exception as e:
        print(f"Error updating Function: {e}")
        return False  # Update failed
    
def delete_fun_tbl(id):
    cursorRead, cursorWrite, engineConRead, engineConWrite, conn = sqliteConfig.sqlite()

    try:
        delete_query = "DELETE FROM Functions WHERE Id = ?"
        cursorWrite.execute(delete_query, (id,))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error deleting Function with ID {id}: {e}")
        return False
    
def insert_fun_tbl(fun, fundec):
    cursorRead, cursorWrite, engineConRead, engineConWrite, conn = sqliteConfig.sqlite()

    try:
        insert_query = "INSERT INTO Functions (FunctionName, FunctionDescription) VALUES (?, ?)"
        cursorWrite.execute(insert_query, (fun, fundec))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error inserting new function: {e}")
        return False


def dropdwn_filter(curent_functionname):
    cursorRead, cursorWrite, engineConRead, engineConWrite, conn = sqliteConfig.sqlite()

    try:
        
        # Step 1: Get the function ID from the functions table
        query = "SELECT Id FROM Functions WHERE FunctionName = ?"
        cursorRead.execute(query, (curent_functionname,))
        row = cursorRead.fetchone()
        
        if row:
            function_id = row[0]
        else:
            return None  # Function name not found
        
        # Step 2: Use the function ID to query Function_Data
        query = """
            SELECT id AS id, Objects, DefaultValues, WorksheetColumnName
            FROM Function_Data
            WHERE FunctionId = ?
        """
        df = pd.read_sql_query(query, engineConRead, params=(function_id,))
        print(df)
        df.columns = ["Id", "Objects", "DefaultValues", "WorksheetColumnName"]

        return df

    except Exception as e:
        print(f"Error in dropdwn_filter: {e}")
        return None
    


    