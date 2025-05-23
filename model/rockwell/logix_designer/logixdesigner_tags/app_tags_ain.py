import pandas as pd

def getRW_AIN(df, nr, Cmd_AlmDint):

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

# Create tags for AIN_UDT
        ain_udt_list = list()
        for i in range(len(df)):
            if str(df.loc[i, "PLC No."]) == str(nr):               
                ain_udt_dict = {'TYPE': 'TAG',
                            'SCOPE': '',
                            'NAME' : f'{df.loc[i, "Tag"]}_AIN_UDT',
                            'DESCRIPTION' : f'UDT_IO_AIN : {df.loc[i, "Description"]}',
                            'DATATYPE' : 'UDT_IO_AIN',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                            }
                ain_udt_list.append(ain_udt_dict)
        ain_udt_df = pd.DataFrame(ain_udt_list)

# Create tags for AIN_CM
        ain_cm_list = list()
        for i in range(len(df)):
            if str(df.loc[i, "PLC No."]) == str(nr):
                ain_cm_dict = {'TYPE': 'TAG',
                            'SCOPE': 'IO',
                            'NAME' : f'{df.loc[i, "Tag"]}_AIN_CM',
                            'DESCRIPTION' : f'CM_AIN : {df.loc[i, "Description"]}',
                            'DATATYPE' : 'CM_AIN',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                            }
                ain_cm_list.append(ain_cm_dict)
        ain_cm_df = pd.DataFrame(ain_cm_list)

# Create a frame with all dataframes, concat them and export the dataframe to .csv
        
        if Cmd_AlmDint:
                frames = [alm_dint_df, ain_udt_df, ain_cm_df]
        elif not Cmd_AlmDint:
              frames = [ain_udt_df, ain_cm_df]
        row = pd.DataFrame({'TYPE': 'TYPE', 'SCOPE': 'SCOPE', 'NAME': 'NAME', 'DESCRIPTION': 'DESCRIPTION', 'DATATYPE': 'DATATYPE', 'SPECIFIER': 'SPECIFIER', 'ATTRIBUTES': 'ATTRIBUTES'}, index=[0])
        result = pd.concat([row] + frames, ignore_index=True)
        result.to_csv('export/rockwell/tags/RA_TAGS_AIN.csv', header = ["0.3","","","","","",""], index=False, sep=',')