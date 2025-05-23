import pandas as pd

def getRW_IO(df, nr, aliasCheckBox):

# Create tags for hardware io
    io_list = list()
    for i in range(len(df)):
        if (str(df.loc[i, "PLC No"]) == str(nr)) and not aliasCheckBox:
            identifier = df.loc[i, "Signal Type"]
            tagPart2 = str(df.loc[i, "TAG Part 2 (# Item)"])
            tagPart2_noDot = tagPart2.split('.', 1)[0]
            tagPart3 = str(df.loc[i, "TAG Part 3 (Function code)"])
            tagPart3_noDot = tagPart3.split('.', 1)[0]
            no_dot_name = f'{tagPart2_noDot}_{tagPart3_noDot}_{df.loc[i, "TAG Part 4 (# Function serial)"]}'
            if identifier == "DI" and pd.notna(df.loc[i, "PLC Address"]):
                io_dict = {'TYPE': 'ALIAS',
                            'SCOPE': '',
                            'NAME' : f'{no_dot_name}_DI_{df.loc[i, "PLC Function"]}',
                            'DESCRIPTION' : f'INPUT : {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]}',
                            'DATATYPE' : '',
                            'SPECIFIER' : f'{df.loc[i, "PLC Address"]}',
                            'ATTRIBUTES' : '(RADIX := Decimal)'
                            }
                io_list.append(io_dict)
            if identifier == "DO" and pd.notna(df.loc[i, "PLC Address"]):
                io_dict = {'TYPE': 'ALIAS',
                            'SCOPE': '',
                            'NAME' : f'{no_dot_name}_DO_{df.loc[i, "PLC Function"]}',
                            'DESCRIPTION' : f'OUTPUT : {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]}',
                            'DATATYPE' : '',
                            'SPECIFIER' : f'{df.loc[i, "PLC Address"]}',
                            'ATTRIBUTES' : '(RADIX := Decimal)'
                            }
                io_list.append(io_dict)
            if identifier == "SDI" and pd.notna(df.loc[i, "PLC Address"]):
                io_dict = {'TYPE': 'ALIAS',
                            'SCOPE': '',
                            'NAME' : f'{no_dot_name}_DI_{df.loc[i, "PLC Function"]}',
                            'DESCRIPTION' : f'INPUT : {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]}',
                            'DATATYPE' : '',
                            'SPECIFIER' : f'{df.loc[i, "PLC Address"]}',
                            'ATTRIBUTES' : '(RADIX := Decimal)'
                            }
                io_list.append(io_dict)
            if identifier == "SDO" and pd.notna(df.loc[i, "PLC Address"]):
                io_dict = {'TYPE': 'ALIAS',
                            'SCOPE': '',
                            'NAME' : f'{no_dot_name}_DO_{df.loc[i, "PLC Function"]}',
                            'DESCRIPTION' : f'SAFE OUTPUT : {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]}',
                            'DATATYPE' : '',
                            'SPECIFIER' : f'{df.loc[i, "PLC Address"]}',
                            'ATTRIBUTES' : '(RADIX := Decimal)'
                            }
                io_list.append(io_dict)
            if identifier == "AI" and pd.notna(df.loc[i, "PLC Address"]):
                io_dict = {'TYPE': 'ALIAS',
                            'SCOPE': '',
                            'NAME' : f'{no_dot_name}_AI_{df.loc[i, "PLC Function"]}',
                            'DESCRIPTION' : f'ANALOG IN : {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]}',
                            'DATATYPE' : '',
                            'SPECIFIER' : f'{df.loc[i, "PLC Address"]}',
                            'ATTRIBUTES' : '(RADIX := Decimal)'
                            }
                io_list.append(io_dict)
            if identifier == "AO" and pd.notna(df.loc[i, "PLC Address"]):
                io_dict = {'TYPE': 'ALIAS',
                            'SCOPE': '',
                            'NAME' : f'{no_dot_name}_AO_{df.loc[i, "PLC Function"]}',
                            'DESCRIPTION' : f'ANALOG OUT : {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]}',
                            'DATATYPE' : '',
                            'SPECIFIER' : f'{df.loc[i, "PLC Address"]}',
                            'ATTRIBUTES' : '(RADIX := Decimal)'
                            }
                io_list.append(io_dict)
            if identifier == "PT" and pd.notna(df.loc[i, "PLC Address"]):
                io_dict = {'TYPE': 'ALIAS',
                            'SCOPE': '',
                            'NAME' : f'{no_dot_name}_AI_{df.loc[i, "PLC Function"]}',
                            'DESCRIPTION' : f'ANALOG IN : {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]}',
                            'DATATYPE' : '',
                            'SPECIFIER' : f'{df.loc[i, "PLC Address"]}',
                            'ATTRIBUTES' : '(RADIX := Decimal)'
                            }
                io_list.append(io_dict)
            if identifier == "DI_F_CNT" and pd.notna(df.loc[i, "PLC Address"]):
                io_dict = {'TYPE': 'ALIAS',
                            'SCOPE': '',
                            'NAME' : f'{no_dot_name}_DI_{df.loc[i, "PLC Function"]}',
                            'DESCRIPTION' : f'INPUT : {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]}',
                            'DATATYPE' : '',
                            'SPECIFIER' : f'{df.loc[i, "PLC Address"]}',
                            'ATTRIBUTES' : '(RADIX := Decimal)'
                            }
                io_list.append(io_dict)
            if identifier == "CPX_VO" and pd.notna(df.loc[i, "PLC Address"]):
                io_dict = {'TYPE': 'ALIAS',
                            'SCOPE': '',
                            'NAME' : f'{no_dot_name}_DO_{df.loc[i, "PLC Function"]}',
                            'DESCRIPTION' : f'OUTPUT : {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]}',
                            'DATATYPE' : '',
                            'SPECIFIER' : f'{df.loc[i, "PLC Address"]}',
                            'ATTRIBUTES' : '(RADIX := Decimal)'
                            }
                io_list.append(io_dict)
            if identifier == "CPX_DI" and pd.notna(df.loc[i, "PLC Address"]):
                io_dict = {'TYPE': 'ALIAS',
                            'SCOPE': '',
                            'NAME' : f'{no_dot_name}_DI_{df.loc[i, "PLC Function"]}',
                            'DESCRIPTION' : f'INPUT : {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]}',
                            'DATATYPE' : '',
                            'SPECIFIER' : f'{df.loc[i, "PLC Address"]}',
                            'ATTRIBUTES' : '(RADIX := Decimal)'
                            }
                io_list.append(io_dict)
            if identifier == "CPX_AO" and pd.notna(df.loc[i, "PLC Address"]):
                io_dict = {'TYPE': 'ALIAS',
                            'SCOPE': '',
                            'NAME' : f'{no_dot_name}_AO_{df.loc[i, "PLC Function"]}',
                            'DESCRIPTION' : f'ANALOG OUT : {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]}',
                            'DATATYPE' : '',
                            'SPECIFIER' : f'{df.loc[i, "PLC Address"]}',
                            'ATTRIBUTES' : '(RADIX := Decimal)'
                            }
            if identifier == "MSG":
                io_dict = {'TYPE': 'TAG',
                            'SCOPE': '',
                            'NAME' : f'{no_dot_name}_MSG_{df.loc[i, "PLC Function"]}',
                            'DESCRIPTION' : f'BOOL : {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]}',
                            'DATATYPE' : 'BOOL',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(RADIX := Decimal)'
                            }
                io_list.append(io_dict)

        # NO ALIAS
        elif (str(df.loc[i, "PLC No"]) == str(nr)) and aliasCheckBox:
            identifier = df.loc[i, "Signal Type"]
            tagPart2 = str(df.loc[i, "TAG Part 2 (# Item)"])
            tagPart2_noDot = tagPart2.split('.', 1)[0]
            tagPart3 = str(df.loc[i, "TAG Part 3 (Function code)"])
            tagPart3_noDot = tagPart3.split('.', 1)[0]
            no_dot_name = f'{tagPart2_noDot}_{tagPart3_noDot}_{df.loc[i, "TAG Part 4 (# Function serial)"]}'
            if identifier == "DI":
                io_dict = {'TYPE': 'TAG',
                            'SCOPE': '',
                            'NAME' : f'{no_dot_name}_DI_{df.loc[i, "PLC Function"]}',
                            'DESCRIPTION' : f'INPUT : {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]}',
                            'DATATYPE' : 'BOOL',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                            }
                io_list.append(io_dict)
            if identifier == "DO":
                io_dict = {'TYPE': 'TAG',
                            'SCOPE': '',
                            'NAME' : f'{no_dot_name}_DO_{df.loc[i, "PLC Function"]}',
                            'DESCRIPTION' : f'OUTPUT : {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]}',
                            'DATATYPE' : 'BOOL',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                            }
                io_list.append(io_dict)
            if identifier == "SDI":
                io_dict = {'TYPE': 'TAG',
                            'SCOPE': '',
                            'NAME' : f'{no_dot_name}_DI_{df.loc[i, "PLC Function"]}',
                            'DESCRIPTION' : f'INPUT : {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]}',
                            'DATATYPE' : 'BOOL',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Safety, Constant := false, ExternalAccess := Read/Write)'
                            }
                io_list.append(io_dict)
            if identifier == "SDO":
                io_dict = {'TYPE': 'TAG',
                            'SCOPE': '',
                            'NAME' : f'{no_dot_name}_DO_{df.loc[i, "PLC Function"]}',
                            'DESCRIPTION' : f'SAFE OUTPUT : {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]}',
                            'DATATYPE' : 'BOOL',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Safety, Constant := false, ExternalAccess := Read/Write)'
                            }
                io_list.append(io_dict)
            if identifier == "AI":
                io_dict = {'TYPE': 'TAG',
                            'SCOPE': '',
                            'NAME' : f'{no_dot_name}_AI_{df.loc[i, "PLC Function"]}',
                            'DESCRIPTION' : f'ANALOG IN : {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]}',
                            'DATATYPE' : 'BOOL',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                            }
                io_list.append(io_dict)
            if identifier == "AO":
                io_dict = {'TYPE': 'TAG',
                            'SCOPE': '',
                            'NAME' : f'{no_dot_name}_AO_{df.loc[i, "PLC Function"]}',
                            'DESCRIPTION' : f'ANALOG OUT : {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]}',
                            'DATATYPE' : 'BOOL',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                            }
                io_list.append(io_dict)
            if identifier == "PT":
                io_dict = {'TYPE': 'TAG',
                            'SCOPE': '',
                            'NAME' : f'{no_dot_name}_AI_{df.loc[i, "PLC Function"]}',
                            'DESCRIPTION' : f'ANALOG IN : {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]}',
                            'DATATYPE' : 'BOOL',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                            }
                io_list.append(io_dict)
            if identifier == "DI_F_CNT":
                io_dict = {'TYPE': 'TAG',
                            'SCOPE': '',
                            'NAME' : f'{no_dot_name}_DI_{df.loc[i, "PLC Function"]}',
                            'DESCRIPTION' : f'INPUT : {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]}',
                            'DATATYPE' : 'BOOL',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                            }
                io_list.append(io_dict)
            if identifier == "CPX_VO":
                io_dict = {'TYPE': 'TAG',
                            'SCOPE': '',
                            'NAME' : f'{no_dot_name}_DO_{df.loc[i, "PLC Function"]}',
                            'DESCRIPTION' : f'OUTPUT : {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]}',
                            'DATATYPE' : 'BOOL',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                            }
                io_list.append(io_dict)
            if identifier == "CPX_DI":
                io_dict = {'TYPE': 'TAG',
                            'SCOPE': '',
                            'NAME' : f'{no_dot_name}_DI_{df.loc[i, "PLC Function"]}',
                            'DESCRIPTION' : f'INPUT : {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]}',
                            'DATATYPE' : 'BOOL',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                            }
                io_list.append(io_dict)
            if identifier == "CPX_AO":
                io_dict = {'TYPE': 'TAG',
                            'SCOPE': '',
                            'NAME' : f'{no_dot_name}_AO_{df.loc[i, "PLC Function"]}',
                            'DESCRIPTION' : f'ANALOG OUT : {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]}',
                            'DATATYPE' : 'BOOL',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                            }
            if identifier == "MSG":
                io_dict = {'TYPE': 'TAG',
                            'SCOPE': '',
                            'NAME' : f'{no_dot_name}_MSG_{df.loc[i, "PLC Function"]}',
                            'DESCRIPTION' : f'BOOL : {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]}',
                            'DATATYPE' : 'BOOL',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                            }
                io_list.append(io_dict)
    io_df = pd.DataFrame(io_list)

# Create a frame with all dataframes, concat them and export the dataframe to .csv
    frames = [io_df]
    row = pd.DataFrame({'TYPE': 'TYPE', 'SCOPE': 'SCOPE', 'NAME': 'NAME', 'DESCRIPTION': 'DESCRIPTION', 'DATATYPE': 'DATATYPE', 'SPECIFIER': 'SPECIFIER', 'ATTRIBUTES': 'ATTRIBUTES'}, index=[0])
    result = pd.concat([row] + frames, ignore_index=True)
    result.to_csv('export/rockwell/tags/RA_TAGS_IO.csv', header=["0.3", "", "", "", "", "", ""], index=False, sep=',')