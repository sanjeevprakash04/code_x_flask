import pandas as pd

def getRW_ModuleSts(df, nr):

# Create tags for ModuleSts_AOI
        modulests_list = list()
        for i in range(len(df)):
            if str(df.loc[i, "PLC No."]) == str(nr):
                tagPart2 = df.loc[i, "Tag Part 2"]
                tagPart2_noDot = tagPart2.split('.', 1)[0]
                tag_name = f'{tagPart2_noDot}_{df.loc[i, "Tag Part 3"]}'
                modulests_dict = {'TYPE': 'TAG',
                            'SCOPE': 'P00_Main',
                            'NAME' : f'{tag_name}_ModuleSts_AOI',
                            'DESCRIPTION' : '',
                            'DATATYPE' : 'F_ModuleStatus',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                            }
                modulests_list.append(modulests_dict)
        modulests_df = pd.DataFrame(modulests_list)

# Create tags for EntrySts_Node
        entrysts_list = list()
        for i in range(len(df)):
            if str(df.loc[i, "PLC No."]) == str(nr):
                tagPart2 = df.loc[i, "Tag Part 2"]
                tagPart2_noDot = tagPart2.split('.', 1)[0]
                tag_name = f'{tagPart2_noDot}_{df.loc[i, "Tag Part 3"]}'
                entrysts_dict = {'TYPE': 'TAG',
                            'SCOPE': 'P00_Main',
                            'NAME' : f'{tag_name}_EntrySts_Node',
                            'DESCRIPTION' : '',
                            'DATATYPE' : 'DINT',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                            }
                entrysts_list.append(entrysts_dict)
        entrysts_df = pd.DataFrame(entrysts_list)

# Create a frame with all dataframes, concat them and export the dataframe to .csv
        frames = [modulests_df, entrysts_df]
        row = pd.DataFrame({'TYPE': 'TYPE', 'SCOPE': 'SCOPE', 'NAME': 'NAME', 'DESCRIPTION': 'DESCRIPTION', 'DATATYPE': 'DATATYPE', 'SPECIFIER': 'SPECIFIER', 'ATTRIBUTES': 'ATTRIBUTES'}, index=[0])
        result = pd.concat([row] + frames, ignore_index=True)
        result.to_csv('export/rockwell/tags/RA_TAGS_ModuleSts.csv', header = ["0.3","","","","","",""], index=False, sep=',')