from ast import Not
from cmath import isnan
import pandas as pd

df = pd.read_excel(r'export/worksheet/RA_Worksheet.xlsx', 'IO List')

file = open(f'export/AreaNames.txt', "w+")

def isNaN(string):
    return string != string

areaNames = []
finalArea = str()
# for i in range(len(df)):
#     if str(df.iloc[i, 0]) == "1" and pd.notna(df.iloc[i, 6]):
#         area = df.iloc[i, 6]
#         if area not in areaNames:
#             areaNames.append(area)
#             file.write(f'{area}\n')

for i in range(len(df)):
    if str(df.iloc[i, 0]) == "1" and pd.notna(df.iloc[i, 6]):
        area1 = df.iloc[i]['Unnamed: 7']
        area2 = df.iloc[i+1]['Unnamed: 7']
        area1Sort = df.iloc[i]['Unnamed: 1']
        area2_sort = df.iloc[i+1]['Unnamed: 1']
        if isNaN(area2):
            finalArea = area1
        elif not isNaN(area2) and area2_sort == 1:
            finalArea = area2
    if finalArea not in areaNames:
        areaNames.append(finalArea)
        file.write(f'{finalArea}\n')

file.close()