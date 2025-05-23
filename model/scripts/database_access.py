import pandas as pd
from sqlalchemy import create_engine


engine = create_engine("access+pyodbc://@MSAccessDatabase")

def ExportToDB():

    filepath = r'Export/worksheet/Worksheet.xlsx'
    df = pd.read_excel(filepath, 'FRQ')

    datadict = {}

    cmno_list = [df.loc[i, "CM No"] for i in range(len(df))]
    tag_list = [df.loc[i, "Tag"] for i in range(len(df))]
    desc_list = [df.loc[i, "Description"] for i in range(len(df))]
    eu_list = [df.loc[i, "EU"] for i in range(len(df))]
    mineu_list = [df.loc[i, "Min EU"] for i in range(len(df))]
    maxeu_list = [df.loc[i, "Max EU"] for i in range(len(df))]

    datadict = {'cmNo' : cmno_list, 'tagName' : tag_list, 'description' : desc_list, 'eu' : eu_list, 'minEU' : mineu_list, 'maxEU' : maxeu_list}

    dfdata = pd.DataFrame(datadict)
    dfdata.fillna(0, inplace=True)

        # appending new data frame
    # to existing data frame
    dfdata.to_sql('tblFRQ', con = engine, if_exists = 'append')
    
    # run a sql query
    # print(engine.execute("SELECT * FROM tblFRQ").fetchall())

    

ExportToDB()