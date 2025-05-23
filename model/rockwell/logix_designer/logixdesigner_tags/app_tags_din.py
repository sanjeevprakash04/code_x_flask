import pandas as pd

def getRW_DIN(df, nr, Cmd_AlmDint):

# Create tags for ALM_DINT
        if Cmd_AlmDint:
                alm_dint_list = list()
                for i in range(len(df)):
                        if str(df.loc[i, "PLC No."]) == str(nr): 
                                alm_dint_dict = {'TYPE': 'TAG',
                                        'SCOPE': '',
                                        'NAME' : f'{df.loc[i, "Tag"]}_ALM_DINT',
                                        'DESCRIPTION' : f'ALM : {df.loc[i, "Description"]}',
                                        'DATATYPE' : 'DINT',
                                        'SPECIFIER' : '',
                                        'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                                        }
                                alm_dint_list.append(alm_dint_dict)
                        alm_dint_df = pd.DataFrame(alm_dint_list)

# Create tags for DIN_UDT
        din_udt_list = list()
        for i in range(len(df)):
            if str(df.loc[i, "PLC No."]) == str(nr):
                din_udt_dict = {'TYPE': 'TAG',
                            'SCOPE': '',
                            'NAME' : f'{df.loc[i, "Tag"]}_DIN_UDT',
                            'DESCRIPTION' : f'UDT_IO_DIN : {df.loc[i, "Description"]}',
                            'DATATYPE' : 'UDT_IO_DIN',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                            }
                din_udt_list.append(din_udt_dict)
        din_udt_df = pd.DataFrame(din_udt_list)

# Create tags for DIN_CM
        din_cm_list = list()
        for i in range(len(df)):
            if str(df.loc[i, "PLC No."]) == str(nr):
                din_cm_dict = {'TYPE': 'TAG',
                            'SCOPE': 'IO',
                            'NAME' : f'{df.loc[i, "Tag"]}_DIN_CM',
                            'DESCRIPTION' : f'CM_DIN : {df.loc[i, "Description"]}',
                            'DATATYPE' : 'CM_DIN',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                            }
                din_cm_list.append(din_cm_dict)
        din_cm_df = pd.DataFrame(din_cm_list)

# Create a frame with all dataframes, concat them and export the dataframe to .csv
        if Cmd_AlmDint:
                frames = [alm_dint_df, din_udt_df, din_cm_df]
        elif not Cmd_AlmDint:
              frames = [din_udt_df, din_cm_df]
        row = pd.DataFrame({'TYPE': 'TYPE', 'SCOPE': 'SCOPE', 'NAME': 'NAME', 'DESCRIPTION': 'DESCRIPTION', 'DATATYPE': 'DATATYPE', 'SPECIFIER': 'SPECIFIER', 'ATTRIBUTES': 'ATTRIBUTES'}, index=[0])
        result = pd.concat([row] + frames, ignore_index=True)
        result.to_csv('export/rockwell/tags/RA_TAGS_DIN.csv',  header = ["0.3","","","","","",""], index=False, sep=',')