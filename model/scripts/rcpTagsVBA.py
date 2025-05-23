import pandas as pd

df = pd.read_excel(r'examples/RA_RCPTags.xlsx', 'RCP')

file = open(f'export/ftseTags/RCPTagsVBA.txt', "w+")
itemNr = -1

for i in range(len(df)):
    itemNr = itemNr + 1
    tagName= df.iloc[i, 6]
    file.write(f'   OPCItem({itemNr}) = "{{[plc1]Program:RCP.{tagName}.DL}}"\n')



file.close()