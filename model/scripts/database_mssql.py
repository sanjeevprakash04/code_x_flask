import pyodbc
import pandas as pd
import sqlalchemy
import urllib
from sqlalchemy.ext.declarative import declarative_base

def createCon ():
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



    # def createTbls ():
    #     Base = declarative_base()
    #     class InfoDB(Base):
    #         __tablename__ = 'tbl_1'
    #         Id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    #         ItemNumber = sqlalchemy.Column(sqlalchemy.String(length=100))
    #         Description = sqlalchemy.Column(sqlalchemy.String(length=100))
    #         PdfElectSchemaPath = sqlalchemy.Column(sqlalchemy.String(length=100))
    #         PdfElectSchemaPage = sqlalchemy.Column(sqlalchemy.String(length=100))

    #     Base.metadata.create_all(engine)

    #     # Create a session
    #     Session = sqlalchemy.orm.sessionmaker()
    #     Session.configure(bind=engine)
    #     session = Session()

    def loadData ():

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

        dfdata.to_sql('tbl_1', schema='dbo', con = engine, if_exists = 'replace', index=False)
        

        # if not sqlalchemy.inspect(engine).has_table("tbl_1"):
        #     print('Table missing')
    # createTbls()
    loadData()

createCon()