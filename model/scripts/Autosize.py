from openpyxl import load_workbook
import pandas as pd

file_path = 'export/worksheet/RA_Worksheet.xlsx'
wb = load_workbook(file_path)

ws = wb['IO List']
df = pd.DataFrame(ws)
for column in df:
    ws.column_dimensions[column].bestFit = True

wb.save(filename = file_path)