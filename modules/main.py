import pandas as pd

from config import sqliteConfig


def tbl_fun_View():
    # Get connections and cursors from your SQLite config
    cursorRead, cursorWrite, engineConRead, engineConWrite, conn = sqliteConfig.sqlite()
    
    # Define your query
    query = "SELECT * FROM Functions"
    
    # Execute the query and return the result as a DataFrame
    df = pd.read_sql_query(query, engineConRead)
      
    return df

def tbl_fun_data():
    # Get connections and cursors from your SQLite config
    cursorRead, cursorWrite, engineConRead, engineConWrite, conn = sqliteConfig.sqlite()
    
    # Define your query
    query = "SELECT id, Objects, DefaultValues, WorksheetColumnName FROM Function_Data"
    
    # Execute the query and return the result as a DataFrame
    df = pd.read_sql_query(query, engineConRead)
    df.columns = ["Id", "Objects", "DefaultValues", "WorksheetColumnName"]
    return df

def drpdwn_data():
    # Get connections and cursors from your SQLite config
    cursorRead, cursorWrite, engineConRead, engineConWrite, conn = sqliteConfig.sqlite()

    cursorRead.execute(f"SELECT FunctionName FROM Functions")
    col_data = cursorRead.fetchall()
    Data = ["None", "ALL"]
    for data in col_data:
        Data.append(data[0])
        print("Column data : ", Data) 

    return Data
