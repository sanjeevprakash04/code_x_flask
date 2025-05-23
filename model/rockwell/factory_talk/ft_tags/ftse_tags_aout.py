import pandas as pd
import csv
import numpy as np 

def getFTSE_TAG_AOUT(df):
        identifier = "AOUT"

        # Create a textfile and write text in it - file is later exported to csv
        file = open(f'export/rockwell/ftseTags/RA_FTSE_TAGS_{identifier}.csv', "w+", encoding="cp1252")
        file.write(";Tag Type, Tag Name, Tag Description, Read Only, Data Source, Security Code, Alarmed, Native Type, Value Type, Min Analog, Max Analog, Initial Analog, Scale, Offset, DeadBand, Units, Off Label Digital, On Label Digital, Initial Digital, Length String, Initial String, Retentive, Address, System Source Name, System Source Index, RIO Address, Element Size Block, Number Elements Block, Initial Block\n")
        file.write(";###002 - THIS LINE CONTAINS VERSION INFORMATION. DO NOT REMOVE!!!\n\n")
        file.write(";Folders Section (Must define folders before tags)\n")
        file.close()

        # Create folders for tags
        folder_list = list()
        for i in range(len(df)):
            tag_name_raw = f'{df.loc[i, "Tag"]}'
            tag_name = tag_name_raw.replace(".1", "").replace(".2", "").replace(".3", "").replace(".4", "").replace(".5", "")
            folder_dict = {'Tag Type': '"F"',
                    'Tag Name': f'"{tag_name}_{identifier}"',
                    'Tag Description' : '',
                    'Read Only' : '"F"',
                    }
            folder_list.append(folder_dict)
        folder_df = pd.DataFrame(folder_list)


        # Create tags
        tag_list = list()
        for i in range(len(df)):
            tag_name_raw = f'{df.loc[i, "Tag"]}'
            tag_comment_raw = f'{df.loc[i, "Description"]}'
            tag_name = tag_name_raw.replace(".1", "").replace(".2", "").replace(".3", "").replace(".4", "").replace(".5", "")
            tag_comment = tag_comment_raw.replace(",", ".") # Commas are not allowed in .csv files when comma is set as seperator
            tag_adress = f'{df.loc[i, "T. Funk"]}'
            area = f'{df.loc[i, "Area"]}'
            eu = f'{df.loc[i, "EU"]}'
            eu_dict = {'Tag Type': '"S"',
                    'Tag Name': f'"{tag_name}_{identifier}\EU"',
                    'Tag Description' : '"Engineering Unit"',
                    'Read Only' : '"F"',
                    'Data Source' : '"M"',
                    'Security Code' : '"*"',
                    'Alarmed' : '"F"',
                    'Native Type' : '',
                    'Value Type' : '',
                    'Min Analog' : '',
                    'Max Analog' : '',
                    'Initial Analog' : '',
                    'Scale' : '',
                    'Offset' : '',
                    'DeadBand' : '',
                    'Units' : '',
                    'Off Label Digital' : '',
                    'On Label Digital' : '',
                    'Initial Digital' : '',
                    'Length String' : '82',
                    'Initial String' : f'"{eu}"',
                    'Retentive' : '0',
                    'Address' : ''
                    }
            plc_dict = {'Tag Type': '"S"',
                    'Tag Name': f'"{tag_name}_{identifier}\PLC"',
                    'Tag Description' : '"PLC name"',
                    'Read Only' : '"F"',
                    'Data Source' : '"M"',
                    'Security Code' : '"*"',
                    'Alarmed' : '"F"',
                    'Native Type' : '',
                    'Value Type' : '',
                    'Min Analog' : '',
                    'Max Analog' : '',
                    'Initial Analog' : '',
                    'Scale' : '',
                    'Offset' : '',
                    'DeadBand' : '',
                    'Units' : '',
                    'Off Label Digital' : '',
                    'On Label Digital' : '',
                    'Initial Digital' : '',
                    'Length String' : '82',
                    'Initial String' : f'"PLC{df.loc[i, "PLC No."]}"',
                    'Retentive' : '0',
                    'Address' : ''
                    }
            tagAddress_dict = {'Tag Type': '"S"',
                    'Tag Name': f'"{tag_name}_{identifier}\TagAddress"',
                    'Tag Description' : '"PLC IO address"',
                    'Read Only' : '"F"',
                    'Data Source' : '"M"',
                    'Security Code' : '"*"',
                    'Alarmed' : '"F"',
                    'Native Type' : '',
                    'Value Type' : '',
                    'Min Analog' : '',
                    'Max Analog' : '',
                    'Initial Analog' : '',
                    'Scale' : '',
                    'Offset' : '',
                    'DeadBand' : '',
                    'Units' : '',
                    'Off Label Digital' : '',
                    'On Label Digital' : '',
                    'Initial Digital' : '',
                    'Length String' : '82',
                    'Initial String' : f'"{tag_adress}"',
                    'Retentive' : '0',
                    'Address' : ''
                    }
            tagComment_dict = {'Tag Type': '"S"',
                    'Tag Name': f'"{tag_name}_{identifier}\TagComment"',
                    'Tag Description' : '"TAG description"',
                    'Read Only' : '"F"',
                    'Data Source' : '"M"',
                    'Security Code' : '"*"',
                    'Alarmed' : '"F"',
                    'Native Type' : '',
                    'Value Type' : '',
                    'Min Analog' : '',
                    'Max Analog' : '',
                    'Initial Analog' : '',
                    'Scale' : '',
                    'Offset' : '',
                    'DeadBand' : '',
                    'Units' : '',
                    'Off Label Digital' : '',
                    'On Label Digital' : '',
                    'Initial Digital' : '',
                    'Length String' : '82',
                    'Initial String' : f'"{tag_comment}"',
                    'Retentive' : '0',
                    'Address' : ''
                    }
            area_dict = {'Tag Type': '"S"',
                    'Tag Name': f'"{tag_name}_{identifier}\Area"',
                    'Tag Description' : '"Area"',
                    'Read Only' : '"F"',
                    'Data Source' : '"M"',
                    'Security Code' : '"*"',
                    'Alarmed' : '"F"',
                    'Native Type' : '',
                    'Value Type' : '',
                    'Min Analog' : '',
                    'Max Analog' : '',
                    'Initial Analog' : '',
                    'Scale' : '',
                    'Offset' : '',
                    'DeadBand' : '',
                    'Units' : '',
                    'Off Label Digital' : '',
                    'On Label Digital' : '',
                    'Initial Digital' : '',
                    'Length String' : '82',
                    'Initial String' : f'"{area}"',
                    'Retentive' : '0',
                    'Address' : ''
                    }
            tagName_dict = {'Tag Type': '"S"',
                    'Tag Name': f'"{tag_name}_{identifier}\TagName"',
                    'Tag Description' : '"TAG name"',
                    'Read Only' : '"F"',
                    'Data Source' : '"M"',
                    'Security Code' : '"*"',
                    'Alarmed' : '"F"',
                    'Native Type' : '',
                    'Value Type' : '',
                    'Min Analog' : '',
                    'Max Analog' : '',
                    'Initial Analog' : '',
                    'Scale' : '',
                    'Offset' : '',
                    'DeadBand' : '',
                    'Units' : '',
                    'Off Label Digital' : '',
                    'On Label Digital' : '',
                    'Initial Digital' : '2',
                    'Length String' : '82',
                    'Initial String' : f'"+{df.loc[i, "Tag Part 2"]}={df.loc[i, "Tag Part 3"]}-{df.loc[i, "Tag Part 4"]}"',
                    'Retentive' : '0',
                    'Address' : '0'
                    }
            tag_list.append(eu_dict)
            tag_list.append(plc_dict)
            tag_list.append(tagAddress_dict)
            tag_list.append(tagComment_dict)
            tag_list.append(area_dict)
            tag_list.append(tagName_dict)
        tag_df = pd.DataFrame(tag_list)
        
        # Append dataframes to earlier created .csv file.
        folder_df.to_csv(f'export/rockwell/ftseTags/RA_FTSE_TAGS_{identifier}.csv', mode='a', header=False, index=False, sep=',', quoting=csv.QUOTE_NONE, encoding="cp1252")
        file = open(f'export/rockwell/ftseTags/RA_FTSE_TAGS_{identifier}.csv', "a+")
        file.write("\n;Tag Section\n")
        file.close()
        tag_df.to_csv(f'export/rockwell/ftseTags/RA_FTSE_TAGS_{identifier}.csv', mode='a', header=False, index=False, sep=',', quoting=csv.QUOTE_NONE, encoding="cp1252")