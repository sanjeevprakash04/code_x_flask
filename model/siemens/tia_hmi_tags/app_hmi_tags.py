import pandas as pd
import numpy as np

# Generate FB_MTR


def getPLCnr(nr):
    getPLCnr.plcnr = nr

# Create tags for HMI


def GenerateHMITags(df, nr, Name, UDT, Connection, dbNamePrefix):

    Hmi_udt_list = list()

    TagSize = len(df)+1  # Calculate no of Array Tag + One Index tax [0]
    # 2Internal tags (Index tag & FacePlateNo_Visible tag)
    Total_TagSize = TagSize+2

    arrMinIndex = min(df["CM No"]) - 1
    arrMaxIndex = max(df["CM No"]) + 5

    # for i in range(Total_TagSize):
    for i in range(arrMinIndex, arrMaxIndex+2):
        # Generate xxx_Index Internal tag
        if i == arrMaxIndex:  # TagSize:
            Name1 = f'{Name}_Index'
            Connection = '<No Value>'
            PLC_tag = '<No Value>'
            DataType = 'DInt'
            Length = '4'
            Access_Method = '<No Value>'
            Address = '<No Value>'
            Index_tag = '<No Value>'

        # Generate xxx_FacePlateNo_Visible Internal tag
        elif i == arrMaxIndex+1:  # TagSize+1:
            Name1 = f'{Name}_FacePlateNo_Visible'
            Connection = '<No Value>'
            PLC_tag = '<No Value>'
            DataType = 'DInt'
            Length = '4'
            Access_Method = '<No Value>'
            Address = '<No Value>'
            Index_tag = '<No Value>'
        # Generate xxx_0 Multiplexing Tag
        elif i == arrMinIndex:  # i==0:
            Name1 = f'{dbNamePrefix}{Name}_{Name}_{i}'  # f'{Name}_{i}'
            # f'{Name}.{Name}[{i}]'
            PLC_tag = f'{dbNamePrefix}{Name}.{Name}[{i}]'
            DataType = UDT  # f'UDT_CM_{Name}'
            Length = ''
            Access_Method = 'Symbolic access'
            # f'{Name}.{Name}[{Name}_Index]'
            Address = f'{dbNamePrefix}{Name}.{Name}[{Name}_Index]'
            Index_tag = f'{Name}_Index'

        # Generate all array Tag from (1--n)
        else:
            Name1 = f'{dbNamePrefix}{Name}_{Name}_{i}'  # f'{Name}_{i}'
            # f'{Name}.{Name}[{i}]'
            PLC_tag = f'{dbNamePrefix}{Name}.{Name}[{i}]'
            DataType = UDT  # f'UDT_CM_{Name}'
            Length = ''
            Access_Method = 'Symbolic access'
            Address = '<No Value>'
            Index_tag = '<No Value>'

        # Dictionary for TIA HMI tag formats
        Hmi_Tag_dict = {'Name': Name1,
                        'Path': f'CM\\{Name}',
                        'Connection': Connection,
                        'PLC tag': PLC_tag,
                        'DataType': DataType,
                        'Length': Length,
                        'Coding': 'Binary',
                        'Access Method': Access_Method,
                        'Address': Address,
                        'Indirect addressing': 'False',
                        'Index tag': Index_tag,
                        'Start value': '<No Value>',
                        'ID tag': '0',
                        'Display name [en-US]': '<No Value>',
                        'Comment [en-US]': '<No Value>',
                        'Acquisition mode': 'Cyclic in operation',
                        'Acquisition cycle': '1 s',
                        'Limit Upper 2 Type': 'None',
                        'Limit Upper 2': '<No Value>',
                        'Limit Upper 1 Type': 'None',
                        'Limit Upper 1': '<No Value>',
                        'Limit Lower 1 Type': 'None',
                        'Limit Lower 1': '<No Value>',
                        'Limit Lower 2 Type': 'None',
                        'Limit Lower 2': '<No Value>',
                        'Linear scaling': 'False',
                        'End value PLC': '10',
                        'Start value PLC': '0',
                        'End value HMI': '100',
                        'Start value HMI': '0',
                        'Gmp relevant': 'False',
                        'Confirmation Type': 'None',
                        'Mandatory Commenting': 'False'
                        }

        Hmi_udt_list.append(Hmi_Tag_dict)
        Hmi_udt_df = pd.DataFrame(Hmi_udt_list)

    filename = "export/siemens/HMI_Tags/%s_Tags.xlsx" % Name

    Multiplexing_dict = {'HMI Tag name': {0: ''}, 'Multiplex Tag': {0: ''}, 'Index': {0: ''}}
    df_Tag_Properties = pd.DataFrame(Multiplexing_dict)

    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        Hmi_udt_df.to_excel(writer, sheet_name='Hmi Tags', index=False)
        df_Tag_Properties.to_excel(writer, sheet_name='Multiplexing', index=False)

