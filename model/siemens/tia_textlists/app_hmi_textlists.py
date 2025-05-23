import pandas as pd

# def GenerateHmiTextlists(df, nr, Name, NamePrefix):

#     description_list = list()
#     number_list = list()
#     for i in range(len(df)):
#         description_dict = {'Parent'          : f'CM_{Name}_Description',
#                               'From'          : df.loc[i, "CM No"],
#                               'To'            : df.loc[i, "CM No"],
#                               'Text [en-US]'  : f'{df.loc[i, "Description"]}'
#                               }
#         description_list.append(description_dict)
    
#     for i in range(len(df)):
#         number_dict = {'Parent'           : f'CM_{Name}_Item_Numbers',
#                           'From'          : df.loc[i, "CM No"],
#                           'To'            : df.loc[i, "CM No"],
#                           'Text [en-US]'  : f'+{df.loc[i, "Tag Part 2"]}={df.loc[i, "Tag Part 3"]}_{df.loc[i, "Tag Part 4"]}'
#                           }
#         number_list.append(number_dict)
    
    
#     description_df = pd.DataFrame(description_list)
#     number_df = pd.DataFrame(number_list)
#     entry_df = pd.concat([description_df, number_df], ignore_index=True)

#     # Sheet1 - TextList
#     filename = "export/siemens/HMI_Textlist/%s_HMI_Textlists.xlsx" % Name
#     writer = pd.ExcelWriter(filename)
#     listItem_description = {'Name': {0: f'CM_{Name}_Description'}, 'ListRange': {0: 'Decimal'}, 'Comment [en-US]': {0: 'Item description for faceplates'}}
#     listItem_number = {'Name': {0: f'CM_{Name}_Item_Numbers'}, 'ListRange': {0: 'Decimal'}, 'Comment [en-US]': {0: 'Item number for faceplates'}}
#     listItem_description_df = pd.DataFrame(listItem_description)
#     listItem_Number_df = pd.DataFrame(listItem_number)
#     list_df = pd.concat([listItem_description_df, listItem_Number_df], ignore_index=True)
#     list_df.to_excel(writer, sheet_name='TextList', index=False)


#     # Sheet2 - HMI Tags
#     # entry_df.fillna("", inplace=True)
#     entry_df.to_excel(writer, sheet_name='TextListEntry', index=False)

#     writer.save()

def GenerateHmiTextlists(df, nr, Name, NamePrefix):
    description_list = []
    number_list = []

    for i in range(len(df)):
        description_dict = {
            'Name': f'Text_list_entry_{i+1}',
            'Parent': f'CM_{Name}_Description',
            'DefaultEntry': '',
            'Value': df.loc[i, "CM No"],
            'Text [en-US]': f'{df.loc[i, "Description"]}',
            'FieldInfos': ''
        }
        description_list.append(description_dict)

    for i in range(len(df)):
        number_dict = {
            'Name': f'Text_list_entry_{i+1}',
            'Parent': f'CM_{Name}_Item_Numbers',
            'DefaultEntry': '',
            'Value': df.loc[i, "CM No"],
            'Text [en-US]': f'+{df.loc[i, "Tag Part 2"]}={df.loc[i, "Tag Part 3"]}-{df.loc[i, "Tag Part 4"]}',
            'FieldInfos': ''
        }
        number_list.append(number_dict)

    description_df = pd.DataFrame(description_list)
    number_df = pd.DataFrame(number_list)
    entry_df = pd.concat([description_df, number_df], ignore_index=True)

    listItem_description = {
            'Name': [f'CM_{Name}_Description'],
            'ListRange': ['Decimal'],
            'Comment [en-US]': ['Item description for faceplates']
        }
    listItem_number = {
        'Name': [f'CM_{Name}_Item_Numbers'],
        'ListRange': ['Decimal'],
        'Comment [en-US]': ['Item number for faceplates']
    }

    listItem_description_df = pd.DataFrame(listItem_description)
    listItem_Number_df = pd.DataFrame(listItem_number)
    list_df = pd.concat([listItem_description_df, listItem_Number_df], ignore_index=True)

    filename = f"export/siemens/HMI_Textlist/{Name}_HMI_Textlists.xlsx"
    with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
        list_df.to_excel(writer, sheet_name='TextList', index=False)
        entry_df.to_excel(writer, sheet_name='TextListEntry', index=False)
        # TIA Portal requires custom properties to be set in the .xlsx file
        writer.book.set_custom_property('TIA_Version', '1.1')
