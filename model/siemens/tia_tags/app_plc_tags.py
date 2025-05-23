import pandas as pd
import numpy as np

def getPLCTags(df, nr):

    mtr_udt_list = list()
    global tagAddress
    tagAddress = ''

    for i in range(len(df)):

        if pd.isnull(df.loc[i]["PLC Tag Name"]) == False:

            if df.loc[i]["Signal Type"] == "DI":
                tagAddress = f'%I{df.loc[i]["PLC Address"]}.{df.loc[i]["PLC Bit address"]}'
                dataType = "Bool"
            elif df.loc[i]["Signal Type"] == "SDI":
                tagAddress = f'%I{df.loc[i]["PLC Address"]}.{df.loc[i]["PLC Bit address"]}'
                dataType = "Bool"
            elif df.loc[i]["Signal Type"] == "AI":
                tagAddress = f'%IW{df.loc[i]["PLC Address"]}'
                dataType = "Int"
            elif df.loc[i]["Signal Type"] == "DO":
                tagAddress = f'%Q{df.loc[i]["PLC Address"]}.{df.loc[i]["PLC Bit address"]}'
                dataType = "Bool"
            elif df.loc[i]["Signal Type"] == "SDO":
                tagAddress = f'%I{df.loc[i]["PLC Address"]}.{df.loc[i]["PLC Bit address"]}'
                dataType = "Bool"
            elif df.loc[i]["Signal Type"] == "AO":
                tagAddress = f'%QW{df.loc[i]["PLC Address"]}'
                dataType = "Int"
            else:
                tagAddress = ''
                dataType = ''

            mtr_udt_dict = {'Name': df.loc[i]["PLC Tag Name"],
                            'Path': "IO",
                            'Data Type': dataType,
                            'Logical Address': tagAddress,
                            'Comment': f'{df.loc[i]["Component Description"]}-{df.loc[i]["Process Description"]}',
                            'Hmi Visible': 'True',
                            'Hmi Accessible': 'True',
                            'Hmi Writeable': 'True',
                            'Typeobject ID': '',
                            'Version ID': ''
                            }
            mtr_udt_list.append(mtr_udt_dict)
            mtr_udt_df = pd.DataFrame(mtr_udt_list)

    Tag_Properties = {'Path': {0: "IO"},
                      'BelongsToUnit': '',
                      'Accessibility': ''
                      }
    df_Tag_Properties = pd.DataFrame(Tag_Properties)

    filepath = f'export/siemens/PLC_Tags/Plc_Tags.xlsx'
    with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
        mtr_udt_df.to_excel(writer, sheet_name='PLC Tags', index=False)
        df_Tag_Properties.to_excel(writer, sheet_name='TagTable Properties', index=False)
