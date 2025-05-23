import pandas as pd

def getRW_SAFE(df, nr):

# Create tags for AOI_SAFETY_ESTOP
        aoi_safe_list = list()
        for i in range(len(df)):
            if str(df.loc[i, "PLC No."]) == str(nr):
                aoi_safe_dict = {'TYPE': 'TAG',
                        'SCOPE': 'IO',
                        'NAME' : f'{df.loc[i, "Tag"]}_ESTOP_AOI',
                        'DESCRIPTION' : f'AOI_SAFETY_ESTOP : {df.loc[i, "Tag Part 2"]}',
                        'DATATYPE' : 'AOI_SAFETY_ESTOP',
                        'SPECIFIER' : '',
                        'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                        }
                aoi_safe_list.append(aoi_safe_dict)
        aoi_safe_df = pd.DataFrame(aoi_safe_list)

# Create tags for ESTOP_UDT
        udt_safe_list = list()
        for i in range(len(df)):
            if str(df.loc[i, "PLC No."]) == str(nr):
                udt_safe_dict = {'TYPE': 'TAG',
                        'SCOPE': '',
                        'NAME' : f'{df.loc[i, "Tag"]}_ESTOP_UDT',
                        'DESCRIPTION' : f'SAFE INPUT : {df.loc[i, "Description"]}',
                        'DATATYPE' : 'EMERGENCY_STOP',
                        'SPECIFIER' : '',
                        'ATTRIBUTES' : '(Class := Safety, Constant := false, ExternalAccess := Read/Write)'
                        }
                udt_safe_list.append(udt_safe_dict)
        udt_safe_df = pd.DataFrame(udt_safe_list)

# Create a frame with all dataframes, concat them and export the dataframe to .csv
        frames = [aoi_safe_df, udt_safe_df]
        row = pd.DataFrame({'TYPE': 'TYPE', 'SCOPE': 'SCOPE', 'NAME': 'NAME', 'DESCRIPTION': 'DESCRIPTION', 'DATATYPE': 'DATATYPE', 'SPECIFIER': 'SPECIFIER', 'ATTRIBUTES': 'ATTRIBUTES'}, index=[0])
        result = pd.concat([row] + frames, ignore_index=True)
        result.to_csv('export/rockwell/tags/RA_TAGS_SAFE.csv', header = ["0.3","","","","","",""], index=False, sep=',')