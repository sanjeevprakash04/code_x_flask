import pandas as pd

def getRW_MTR(df, nr, Cmd_AlmDint):

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

# Create tags for MTR_UDT
        mtr_udt_list = list()
        for i in range(len(df)):
            if str(df.loc[i, "PLC No."]) == str(nr):
                mtr_udt_dict = {'TYPE': 'TAG',
                            'SCOPE': '',
                            'NAME' : f'{df.loc[i, "Tag"]}_MTR_UDT',
                            'DESCRIPTION' : f'UDT_IO_MTR : {df.loc[i, "Description"]}',
                            'DATATYPE' : 'UDT_IO_MTR',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                            }
                mtr_udt_list.append(mtr_udt_dict)
        mtr_udt_df = pd.DataFrame(mtr_udt_list)

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

# Create tags for MTR_CM
        mtr_cm_list = list()
        for i in range(len(df)):
            if str(df.loc[i, "PLC No."]) == str(nr):
                mtr_cm_dict = {'TYPE': 'TAG',
                            'SCOPE': 'IO',
                            'NAME' : f'{df.loc[i, "Tag"]}_MTR_CM',
                            'DESCRIPTION' : f'CM_MTR : {df.loc[i, "Description"]}',
                            'DATATYPE' : 'CM_MTR',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                            }
                mtr_cm_list.append(mtr_cm_dict)
        mtr_cm_df = pd.DataFrame(mtr_cm_list)

# Create tags for CROUT AOI
        crout_aoi_list = list()
        for i in range(len(df)):
            if str(df.loc[i, "PLC No."]) == str(nr):
                no_dot_name = df.loc[i, "Tag"]
                no_dot_name = no_dot_name.replace("MA", "QE")
                no_dot_name = no_dot_name.replace("FC", "QE")
                crout_aoi_dict = {'TYPE': 'TAG',
                            'SCOPE': 'Safety_Z1',
                            'NAME' : f'{no_dot_name}_CROUT_AOI',
                            'DESCRIPTION' : f'SAFE OUTPUT : {df.loc[i, "Description"]}',
                            'DATATYPE' : 'CONFIGURABLE_ROUT',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Safety, Usage := Public, Constant := false, ExternalAccess := Read/Write)'
                            }
                crout_aoi_list.append(crout_aoi_dict)
        crout_aoi_df = pd.DataFrame(crout_aoi_list)

# Create tags safety mapping - standard
        s_map_list = list()
        for i in range(len(df)):
            if str(df.loc[i, "PLC No."]) == str(nr):
                start_fwd = f'{df.loc[i, "Start Forward"]}'
                start_rev = f'{df.loc[i, "Start Reverse"]}'
                emg_fb = f'{df.loc[i, "Emergency Stop Contactor FB"]}'

                if pd.notna(df.loc[i, "Start Forward"]):
                    start_fwd_dict = {'TYPE': 'TAG',
                                'SCOPE': '',
                                'NAME' : f'{start_fwd}_S',
                                'DESCRIPTION' : f'MAPPED: {df.loc[i, "Description"]}',
                                'DATATYPE' : 'BOOL',
                                'SPECIFIER' : '',
                                'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                                }
                    s_map_list.append(start_fwd_dict)
                if pd.notna(df.loc[i, "Start Reverse"]):
                    start_rev_dict = {'TYPE': 'TAG',
                                'SCOPE': '',
                                'NAME' : f'{start_rev}_S',
                                'DESCRIPTION' : f'MAPPED: {df.loc[i, "Description"]}',
                                'DATATYPE' : 'BOOL',
                                'SPECIFIER' : '',
                                'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                                }
                    s_map_list.append(start_rev_dict)
                if pd.notna(df.loc[i, "Emergency Stop Contactor FB"]):
                    emg_fb_dict = {'TYPE': 'TAG',
                                'SCOPE': '',
                                'NAME' : f'{emg_fb}_S',
                                'DESCRIPTION' : f'MAPPED: {df.loc[i, "Description"]}',
                                'DATATYPE' : 'BOOL',
                                'SPECIFIER' : '',
                                'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                                }

                    s_map_list.append(emg_fb_dict)
        s_map_df = pd.DataFrame(s_map_list)

# Create tags safety mapping - safety
        sp_map_list = list()
        for i in range(len(df)):
            if str(df.loc[i, "PLC No."]) == str(nr):
                start_fwd = f'{df.loc[i, "Start Forward"]}'
                start_rev = f'{df.loc[i, "Start Reverse"]}'
                emg_fb = f'{df.loc[i, "Emergency Stop Contactor FB"]}'

                if pd.notna(df.loc[i, "Start Forward"]):
                    start_fwd_sp_dict = {'TYPE': 'TAG',
                                'SCOPE': '',
                                'NAME' : f'{start_fwd}_SP',
                                'DESCRIPTION' : f'MAPPED SAFE: {df.loc[i, "Description"]}',
                                'DATATYPE' : 'BOOL',
                                'SPECIFIER' : '',
                                'ATTRIBUTES' : '(Class := Safety, Constant := false, ExternalAccess := Read/Write)'
                                }
                    sp_map_list.append(start_fwd_sp_dict)
                if pd.notna(df.loc[i, "Start Reverse"]):
                    start_rev_sp_dict = {'TYPE': 'TAG',
                                'SCOPE': '',
                                'NAME' : f'{start_rev}_SP',
                                'DESCRIPTION' : f'MAPPED SAFE: {df.loc[i, "Description"]}',
                                'DATATYPE' : 'BOOL',
                                'SPECIFIER' : '',
                                'ATTRIBUTES' : '(Class := Safety, Constant := false, ExternalAccess := Read/Write)'
                                }
                    sp_map_list.append(start_rev_sp_dict)
                if pd.notna(df.loc[i, "Emergency Stop Contactor FB"]):
                    emg_fb_sp_dict = {'TYPE': 'TAG',
                                'SCOPE': '',
                                'NAME' : f'{emg_fb}_SP',
                                'DESCRIPTION' : f'MAPPED SAFE: {df.loc[i, "Description"]}',
                                'DATATYPE' : 'BOOL',
                                'SPECIFIER' : '',
                                'ATTRIBUTES' : '(Class := Safety, Constant := false, ExternalAccess := Read/Write)'
                                }

                    sp_map_list.append(emg_fb_sp_dict)
        sp_map_df = pd.DataFrame(sp_map_list)

# Create tags for enable crout
        enable_list = list()
        for i in range(len(df)):
            if str(df.loc[i, "PLC No."]) == str(nr):
                no_dot_name = df.loc[i, "Tag"]
                no_dot_name = no_dot_name.replace("MA", "QE")
                no_dot_name = no_dot_name.replace("FC", "QE")
                enable_dict = {'TYPE': 'TAG',
                            'SCOPE': 'Safety_Z1',
                            'NAME' : f'{no_dot_name}_Enable',
                            'DESCRIPTION' : '',
                            'DATATYPE' : 'BOOL',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Safety, Constant := false, ExternalAccess := Read/Write)'
                            }
                enable_list.append(enable_dict)
        enable_df = pd.DataFrame(enable_list)

# Create a frame with all dataframes, concat them and export the dataframe to .csv
        if Cmd_AlmDint:
                frames = [alm_dint_df, mtr_udt_df, safetyOK_df, sf_ok_df, mtr_cm_df, crout_aoi_df, s_map_df, sp_map_df, enable_df]
        elif not Cmd_AlmDint:
              frames = [mtr_udt_df, safetyOK_df, sf_ok_df, mtr_cm_df, crout_aoi_df, s_map_df, sp_map_df, enable_df]
        row = pd.DataFrame({'TYPE': 'TYPE', 'SCOPE': 'SCOPE', 'NAME': 'NAME', 'DESCRIPTION': 'DESCRIPTION', 'DATATYPE': 'DATATYPE', 'SPECIFIER': 'SPECIFIER', 'ATTRIBUTES': 'ATTRIBUTES'}, index=[0])
        result = pd.concat([row] + frames, ignore_index=True)
        result.to_csv('export/rockwell/tags/RA_TAGS_MTR.csv', header = ["0.3","","","","","",""], index=False, sep=',')