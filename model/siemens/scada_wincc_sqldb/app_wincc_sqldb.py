import pandas as pd
import numpy as np
# import xlsxwriter

import PyPDF2
import re
import os

##########################################################


def searchTextInPdffile(pdf_file, searchKey):
    obj = PyPDF2.PdfReader(pdf_file)
    pgno = len(obj.pages)
    found = False
    for page in range(0, pgno):
        PgOb = obj.pages[page]
        Text = PgOb.extract_text()

        if searchKey in Text:
            found = True
            pdfPageNo = page+1
            return pdfPageNo
            break
    if found == False:
        return " "
#########################################################


def searchTextInPdf(df1, folderPath, refPdfPath):

    df = df1.copy()

    for i in range(len(df)):
        Item = df.loc[i]['ItemNumber']
        # decode ItemNumber
        words1 = Item.split('+', 1)  # Use 2nd word after "+"
        Items = words1[1].split('=')  # Split into 2 word "=" as a delimiter
        words2 = Items[0].split('.')  # Use only 1st word before "."
        Items[0] = words2[0]
        # print(Items)
        found = False
        for filename in os.listdir(folderPath):
            if Items[0] in filename:
                pdf_file = open(os.path.join(folderPath, filename), 'rb')
                found = True

                pgNo = searchTextInPdffile(pdf_file, Items[1])
                print(pgNo)

                df.loc[i, "PdfElectSchemaPage"] = pgNo

                if refPdfPath != "":
                    path = os.path.join(refPdfPath, filename)
                    pathFormat = (path.replace("\\", "\\\\"))
                    df.loc[i, "PdfElectSchemaPath"] = pathFormat
                else:
                    df.loc[i, "PdfElectSchemaPath"] = pdf_file.name

        if found == False:
            print("pdf_file not found")

    return df

#########################################################


# Create Sqldb for WinCC 7.5 Scada

def GenerateWinccSqldb(df, nr, Name, electDocFilepath, refPdfPath, objects, column_dict, column_defaultvalue_dict=None):

    if column_defaultvalue_dict == None:
        column_defaultvalue_dict = {}

    Scada_Sqldb_list = list()

    for i in range(len(df)):

        Scada_Sqldb_dict = {}
        for obj in objects:
            if obj == "Id":
                Scada_Sqldb_dict[obj] = df.loc[i]["CM No"]
            elif obj == "ItemNumber":
                Scada_Sqldb_dict[obj] = f'+{df.loc[i]["Tag Part 2"]}={df.loc[i]["Tag Part 3"]}-{df.loc[i]["Tag Part 4"]}'
            elif obj in column_defaultvalue_dict:
                Scada_Sqldb_dict[obj] = column_defaultvalue_dict[obj]
            elif obj in column_dict:
                Scada_Sqldb_dict[obj] = df.loc[i][column_dict[obj]]
            else:
                Scada_Sqldb_dict[obj] = ""

        Scada_Sqldb_list.append(Scada_Sqldb_dict)
        Scada_Sqldb_df = pd.DataFrame(Scada_Sqldb_list)

    folderPath = (electDocFilepath.replace('/', "\\\\"))
    Scada_Sqldb_df1 = searchTextInPdf(Scada_Sqldb_df, folderPath, refPdfPath)

    filename = "export/siemens/SCADA_Database/%s_Sql_db.xlsx" % Name
    sheetname = "DB_%s" % Name

    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        Scada_Sqldb_df1.to_excel(writer, sheet_name=sheetname, index=False)
