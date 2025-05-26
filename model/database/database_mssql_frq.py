import pandas as pd
import sqlalchemy
import urllib
from sqlalchemy.ext.declarative import declarative_base

def _createCon ():
    # server = 'myserver,port' # to specify an alternate port
    server = '192.168.0.109,1433' 
    database = 'infodb' 
    username = 'root' 
    password = 'CedasVM' 
    # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
    cnxn = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    engine = sqlalchemy.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(cnxn))

    if engine.connect():
        status = 'Connected to SQL Server successfully'
    else:
        status = 'Could not connect to SQL server'
    print(status)

    pdfElectpath = ""
    pdfVfdpath = ""

    def _loadData ():

        filepath = r'export/worksheet/Siemens_Worksheet.xlsx'
        sheets = ["FRQ", "MTR", "VLV", "DIN", "AIN", "AOUT", "PID", "ALM"]
        df = pd.read_excel(filepath, "FRQ", dtype=object)


        cmno_list = [df.loc[i, "CM No"] for i in range(len(df))]
        tag_list = [df.loc[i, "Tag"] for i in range(len(df))]
        desc_list = [df.loc[i, "Description"] for i in range(len(df))]
        ipAddress_list = [df.loc[i, "IP Address"] for i in range(len(df))]
        pdfElectpath_list = [pdfElectpath for i in range(len(df))]
        pdfElectpage_list = [df.loc[i, "Pdf Elect Schema Page"] for i in range(len(df))]
        pdfVfdpath_list = [pdfVfdpath for i in range(len(df))]
        pdfVfdpage_list = [df.loc[i, "Pdf Vfd Schema Page"] for i in range(len(df))]

        datadict = {'Id' : cmno_list, 'ItemNumber' : tag_list, 'Description' : desc_list, 'IpAddress' : ipAddress_list, 'PdfElectSchemaPath' : pdfElectpath_list, 'PdfElectSchemaPage' : pdfElectpage_list, 'PdfVfdSchemaPath' : pdfVfdpath_list, 'PdfVfdSchemaPage' : pdfVfdpage_list}
        dfdata = pd.DataFrame(datadict)
        dfdata.fillna(0, inplace=True) 

        dfdata.to_sql('FRQ', schema='dbo', con = engine, if_exists = 'replace', index=False)

    _loadData()

_createCon()