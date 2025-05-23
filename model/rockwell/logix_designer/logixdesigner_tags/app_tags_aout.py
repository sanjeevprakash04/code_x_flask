import pandas as pd

def getRW_AOUT(df, nr, Cmd_AlmDint):

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

# Create tags for AOUT_UDT
        aout_udt_list = list()
        for i in range(len(df)):
            if str(df.loc[i, "PLC No."]) == str(nr):
                aout_udt_dict = {'TYPE': 'TAG',
                            'SCOPE': '',
                            'NAME' : f'{df.loc[i, "Tag"]}_AOUT_UDT',
                            'DESCRIPTION' : f'UDT_IO_AOUT : {df.loc[i, "Description"]}',
                            'DATATYPE' : 'UDT_IO_AOUT',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                            }
                aout_udt_list.append(aout_udt_dict)
        aout_udt_df = pd.DataFrame(aout_udt_list)

# Create tags for AOUT_CM
        aout_cm_list = list()
        for i in range(len(df)):
            if str(df.loc[i, "PLC No."]) == str(nr):
                aout_cm_dict = {'TYPE': 'TAG',
                            'SCOPE': 'IO',
                            'NAME' : f'{df.loc[i, "Tag"]}_AOUT_CM',
                            'DESCRIPTION' : f'CM_AOUT : {df.loc[i, "Description"]}',
                            'DATATYPE' : 'CM_AOUT',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                            }
                aout_cm_list.append(aout_cm_dict)
        aout_cm_df = pd.DataFrame(aout_cm_list)

# Create a frame with all dataframes, concat them and export the dataframe to .csv
        if Cmd_AlmDint:
                frames = [alm_dint_df, aout_udt_df, aout_cm_df]
        elif not Cmd_AlmDint:
              frames = [aout_udt_df, aout_cm_df]
        row = pd.DataFrame({'TYPE': 'TYPE', 'SCOPE': 'SCOPE', 'NAME': 'NAME', 'DESCRIPTION': 'DESCRIPTION', 'DATATYPE': 'DATATYPE', 'SPECIFIER': 'SPECIFIER', 'ATTRIBUTES': 'ATTRIBUTES'}, index=[0])
        result = pd.concat([row] + frames, ignore_index=True)
        result.to_csv('export/rockwell/tags/RA_TAGS_AOUT.csv',  header = ["0.3","","","","","",""], index=False, sep=',')