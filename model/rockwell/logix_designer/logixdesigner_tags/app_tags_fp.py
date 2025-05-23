import pandas as pd

def getRW_FP(df, nr):

# Create tags for FP_UDT
        fp_udt_list = list()
        for i in range(len(df)):
                #subIdList = ["1"] # Change depending on what tab ID to generate for
                #subId = f'{df.loc[i, "Tab ID"]}'
                #if subId in subIdList:
                fp_udt_dict = {'TYPE': 'TAG',
                            'SCOPE': '',
                            'NAME' : f'{df.loc[i, "Tag"]}_FP_UDT',
                            'DESCRIPTION' : f'UDT_IO_FP : {df.iloc[i, 4]}',
                            'DATATYPE' : 'UDT_IO_FP',
                            'SPECIFIER' : '',
                            'ATTRIBUTES' : '(Class := Standard, Constant := false, ExternalAccess := Read/Write)'
                            }
                eu_dict = {'TYPE': 'COMMENT:en-US',
                        'SCOPE': '',
                        'NAME' : f'{df.loc[i, "Tag"]}_FP_UDT',
                        'DESCRIPTION' : df.loc[i, "EU"],
                        'DATATYPE' : '',
                        'SPECIFIER' : f'{df.loc[i, "Tag"]}_FP_UDT.EU'
                        }
                plc_dict = {'TYPE': 'COMMENT:en-US',
                        'SCOPE': '',
                        'NAME' : f'{df.loc[i, "Tag"]}_FP_UDT',
                        'DESCRIPTION' : df.loc[i, "PLC No."],
                        'DATATYPE' : '',
                        'SPECIFIER' : f'{df.loc[i, "Tag"]}_FP_UDT.PLC'
                        }
                tagComment_dict = {'TYPE': 'COMMENT:en-US',
                        'SCOPE': '',
                        'NAME' : f'{df.loc[i, "Tag"]}_FP_UDT',
                        'DESCRIPTION' : f'{df.loc[i, "Description"]}',
                        'DATATYPE' : '',
                        'SPECIFIER' : f'{df.loc[i, "Tag"]}_FP_UDT.TagComment'
                        }
                tagAddress_dict = {'TYPE': 'COMMENT:en-US',
                        'SCOPE': '',
                        'NAME' : f'{df.loc[i, "Tag"]}_FP_UDT',
                        'DESCRIPTION' : df.loc[i, "PLC Address"],
                        'DATATYPE' : '',
                        'SPECIFIER' : f'{df.loc[i, "Tag"]}_FP_UDT.TagAddress'
                        }
                tagName_dict = {'TYPE': 'COMMENT:en-US',
                        'SCOPE': '',
                        'NAME' : f'{df.loc[i, "Tag"]}_FP_UDT',
                        'DESCRIPTION' : f'+{df.loc[i, "Tag Part 2"]}={df.loc[i, "Tag Part 3"]}-{df.loc[i, "Tag Part 4"]}',
                        'DATATYPE' : '',
                        'SPECIFIER' : f'{df.loc[i, "Tag"]}_FP_UDT.TagName'
                        }
                fp_udt_list.append(fp_udt_dict)
                fp_udt_list.append(eu_dict)
                fp_udt_list.append(plc_dict)
                fp_udt_list.append(tagComment_dict)
                fp_udt_list.append(tagAddress_dict)
                fp_udt_list.append(tagName_dict)
        fp_udt_df = pd.DataFrame(fp_udt_list)
                
# Create a frame with all dataframes, concat them and export the dataframe to .csv
        frames = [fp_udt_df]
        row = pd.DataFrame({'TYPE': 'TYPE', 'SCOPE': 'SCOPE', 'NAME': 'NAME', 'DESCRIPTION': 'DESCRIPTION', 'DATATYPE': 'DATATYPE', 'SPECIFIER': 'SPECIFIER', 'ATTRIBUTES': 'ATTRIBUTES'}, index=[0])
        result = pd.concat([row] + frames, ignore_index=True)
        result.to_csv('export/rockwell/tags/RA_TAGS_FP.csv', header = ["0.3","","","","","",""],index=False, sep=',')