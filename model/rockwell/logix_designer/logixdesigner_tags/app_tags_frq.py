import pandas as pd

def getRW_FRQ(df, nr, Cmd_AlmDint):

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

# Create tags for FRQ_UDT
        frq_udt_list = list()
        for i in range(len(df)):
            if str(df.loc[i, "PLC No."]) == str(nr):
                frq_udt_dict = {'TYPE': 'TAG',
                            'SCOPE': '',
                            'NAME' : f'{df.loc[i, "Tag"]}_FRQ_UDT',
                            'DESCRIPTION' : f'UDT_IO_FRQ : {df.loc[i, "Description"]} [{df.loc[i, "EU"]}] ({df.loc[i, "Tag Part 2"]})',
                            'DATATYPE' : 'UDT_IO_FRQ',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                            }
                frq_udt_list.append(frq_udt_dict)
        frq_udt_df = pd.DataFrame(frq_udt_list)

# Create tags for SafetyOK
        safetyOK_list = list()
        for i in range(len(df)):
            if str(df.loc[i, "PLC No."]) == str(nr):
                safetyOK_dict = {'TYPE': 'TAG',
                            'SCOPE': 'IO',
                            'NAME' : f'{df.loc[i, "Tag"]}_SafetyOK',
                            'DESCRIPTION' : f'Safety OK',
                            'DATATYPE' : 'BOOL',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                            }
                safetyOK_list.append(safetyOK_dict)
        safetyOK_df = pd.DataFrame(safetyOK_list)

# Create tags for SF_OK
        sf_ok_list = list()
        for i in range(len(df)):
            if str(df.loc[i, "PLC No."]) == str(nr):
                sf_ok_dict = {'TYPE': 'TAG',
                            'SCOPE': 'Safety_Z1',
                            'NAME' : f'{df.loc[i, "Tag"]}_SF_OK',
                            'DESCRIPTION' : f'Safe OK',
                            'DATATYPE' : 'BOOL',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Safety, Usage := Public, Constant := false, ExternalAccess := Read/Write)'
                            }
                sf_ok_list.append(sf_ok_dict)
        sf_ok_df = pd.DataFrame(sf_ok_list)

# Create tags for FRQ_CM
        frq_cm_list = list()
        for i in range(len(df)):
            if str(df.loc[i, "PLC No."]) == str(nr):
                frq_cm_dict = {'TYPE': 'TAG',
                            'SCOPE': 'IO',
                            'NAME' : f'{df.loc[i, "Tag"]}_FRQ_CM',
                            'DESCRIPTION' : f'CM_FRQ : {df.loc[i, "Description"]}',
                            'DATATYPE' : 'CM_FRQ',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                            }
                frq_cm_list.append(frq_cm_dict)
        frq_cm_df = pd.DataFrame(frq_cm_list)

# Create tags for COM_F
        com_f_list = list()
        for i in range(len(df)):
            if str(df.loc[i, "PLC No."]) == str(nr):
                com_f_dict = {'TYPE': 'TAG',
                            'SCOPE': 'IO',
                            'NAME' : f'{df.loc[i, "Tag"]}_COM_F',
                            'DESCRIPTION' : f'{df.loc[i, "FRQ Type"]} : {df.loc[i, "Description"]}',
                            'DATATYPE' : f'F_{df.loc[i, "FRQ Type"]}',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                            }
                com_f_list.append(com_f_dict)
        com_f_df = pd.DataFrame(com_f_list)

# Create tags for COM_UDT
        com_udt_list = list()
        for i in range(len(df)):
            if str(df.loc[i, "PLC No."]) == str(nr):
                com_udt_dict = {'TYPE': 'TAG',
                            'SCOPE': 'IO',
                            'NAME' : f'{df.loc[i, "Tag"]}_COM_UDT',
                            'DESCRIPTION' : f'UDT_IO_FRQ : {df.loc[i, "Description"]}',
                            'DATATYPE' : 'UDT_IO_FRQ_Com',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                            }
                com_udt_list.append(com_udt_dict)
        com_udt_df = pd.DataFrame(com_udt_list)

# Create tags for STO_AOI
        sto_aoi_list = list()
        for i in range(len(df)):
            if str(df.loc[i, "PLC No."]) == str(nr):
                sto_aoi_dict = {'TYPE': 'TAG',
                            'SCOPE': 'Safety_Z1',
                            'NAME' : f'{df.loc[i, "Tag"]}_STO_AOI',
                            'DESCRIPTION' : f'{df.loc[i, "Description"]}',
                            'DATATYPE' : 'AOI_STO_V1_01',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Safety, Constant := false, ExternalAccess := Read/Write)'
                            }
                sto_aoi_list.append(sto_aoi_dict)
        sto_aoi_df = pd.DataFrame(sto_aoi_list)

# Create tags for SF_Enable
        sf_enable_list = list()
        for i in range(len(df)):
            if str(df.loc[i, "PLC No."]) == str(nr):
                sf_enable_dict = {'TYPE': 'TAG',
                            'SCOPE': 'Safety_Z1',
                            'NAME' : f'{df.loc[i, "Tag"]}_SF_Enable',
                            'DESCRIPTION' : f'Enable Output : {df.loc[i, "Description"]}',
                            'DATATYPE' : 'BOOL',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Safety, Constant := false, ExternalAccess := Read/Write)'
                            }
                sf_enable_list.append(sf_enable_dict)
        sf_enable_df = pd.DataFrame(sf_enable_list)

# Create a frame with all dataframes, concat them and export the dataframe to .csv
        if Cmd_AlmDint:
                frames = [alm_dint_df, frq_udt_df, safetyOK_df, sf_ok_df, frq_cm_df, com_f_df, com_udt_df, sto_aoi_df, sf_enable_df]
        elif not Cmd_AlmDint:
              frames = [frq_udt_df, safetyOK_df, sf_ok_df, frq_cm_df, com_f_df, com_udt_df, sto_aoi_df, sf_enable_df]   
        row = pd.DataFrame({'TYPE': 'TYPE', 'SCOPE': 'SCOPE', 'NAME': 'NAME', 'DESCRIPTION': 'DESCRIPTION', 'DATATYPE': 'DATATYPE', 'SPECIFIER': 'SPECIFIER', 'ATTRIBUTES': 'ATTRIBUTES'}, index=[0])
        result = pd.concat([row] + frames, ignore_index=True)
        result.to_csv('export/rockwell/tags/RA_TAGS_FRQ.csv', header = ["0.3","","","","","",""], index=False, sep=',')