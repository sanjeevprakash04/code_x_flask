import pandas as pd
import numpy as np

def RCPSheet():
    df = pd.read_excel(r'examples/RA_Worksheet.xlsx', 'IO List')

    rcp_list = list()
    for i in range(len(df)):
        identifiers = ["FRQ"]
        identifier = df.iloc[i, 78]
        if pd.notna(df.iloc[i, 6]):
            tagName = df.iloc[i, 6]
            tagName = tagName.replace(" ", "")
        if identifier in identifiers:
                rcp_dict = {'PLC'           : '',
                            'SCADA'         : '',
                            'Tag Part 2'    : df.iloc[i, 3],
                            'Tag Part 3'    : df.iloc[i, 4],
                            'Description'   : f'{df.iloc[i, 6]} - {df.iloc[i, 7]}',
                            'Tag Name'      : tagName,
                            'Type'          : 'Motor',
                            'Data Type'     : '',
                            'EU'            : df.iloc[i, 38],
                            'Min'           : df.iloc[i, 39],
                            'Max'           : df.iloc[i, 40],
                            'Tab ID'        : df.iloc[i, 88],
                            'Sub ID'        : df.iloc[i, 111],
                            'Section'       : ''
                            }
                rcp_list.append(rcp_dict)
    rcp_df = pd.DataFrame(rcp_list)


    writer = pd.ExcelWriter(r'export/rcp/RA_RCPTags.xlsx', engine='xlsxwriter') # pylint: disable=abstract-class-instantiated
    rcp_df.to_excel(writer, sheet_name='RCP', index=False)
    for column in rcp_df:
        column_width = max(rcp_df[column].astype(str).map(len).max(), len(column))
        col_idx = rcp_df.columns.get_loc(column)
        writer.sheets['RCP'].set_column(col_idx, col_idx, column_width)

    writer.save()

RCPSheet()