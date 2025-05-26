import pandas as pd

def getSafMapTags(df_import2): #Use "Safety Mapping - Template" as import

    df_io = df_import2.copy()
    df_io = pd.DataFrame(df_import2.iloc[1:, :])
    df = df_io.copy()

# Create tags for S tag - standard tag
    s_tag_list = list()
    for i in range(len(df)):
        tagPart1_noDot = df.loc[i, "Tag name to be safety mapped:"].split('.', 1)[0]
        s_tag_dict = {'TYPE': 'TAG',
                    'SCOPE': '',
                    'NAME' : f'{tagPart1_noDot}_S',
                    'DESCRIPTION' : f'MAPPED : {df.loc[i, "Description:"]}',
                    'DATATYPE' : 'BOOL',
                    'SPECIFIER' : '',
                    'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                    }
        s_tag_list.append(s_tag_dict)
    s_tag_df = pd.DataFrame(s_tag_list)

# Create tags for SP tag - safety tag
    sp_tag_list = list()
    for i in range(len(df)):
        tagPart1_noDot = df.loc[i, "Tag name to be safety mapped:"].split('.', 1)[0]
        sp_tag_dict = {'TYPE': 'TAG',
                    'SCOPE': '',
                    'NAME' : f'{tagPart1_noDot}_SP',
                    'DESCRIPTION' : f'MAPPED SAFE : {df.loc[i, "Description:"]}',
                    'DATATYPE' : 'BOOL',
                    'SPECIFIER' : '',
                    'ATTRIBUTES' : '(Class := Safety, Constant := false, ExternalAccess := Read/Write)'
                    }
        sp_tag_list.append(sp_tag_dict)
    sp_tag_df = pd.DataFrame(sp_tag_list)

# Create a frame with all dataframes, concat them and export the dataframe to .csv
    frames = [s_tag_df, sp_tag_df]
    row = pd.DataFrame({'TYPE': 'TYPE', 'SCOPE': 'SCOPE', 'NAME': 'NAME', 'DESCRIPTION': 'DESCRIPTION', 'DATATYPE': 'DATATYPE', 'SPECIFIER': 'SPECIFIER', 'ATTRIBUTES': 'ATTRIBUTES'}, index=[0])
    result = pd.concat([row] + frames, ignore_index=True)
    result.to_csv('export/rockwell/tags/RA_TAGS_SafetyMapping.csv', header = ["0.3","","","","","",""], index=False, sep=',')