import pandas as pd

def generateCmNo():

    df_import = pd.read_excel(r'examples/IO_List.xlsm', 'IO list')

    df_io = df_import.copy()
    df_io = pd.DataFrame(df_import.iloc[2:, 1:])
    df = df_io.copy()
# ----------------Autogenerate Generator Config Number----------------
    identifiers = ["FRQ", "MTR", "AIN", "AOUT", "DIN", "PID", "ALM", "VLV"]

    ##### FRQ #####
    # num_count = 0
    # next_num = 0
    # num_count_list = list()
    # for row in df.itertuples():
    
        # identifier = getattr(row, "Common Control modules")
        # if identifier == "FRQ":
        #     num_count = getattr(row, "Unnamed: 96")
        #     num_count_list.append(num_count)

    # for i in range(len(df)):
    #     identifier = df.iloc[i, 78]
    #     if identifier == "FRQ":
    #         num_count = df.iloc[i, 95]
    #         num_count_list.append(num_count)

    print(df.apply(lambda row: row["Common Control modules"], axis = 1))

    # num_count_list = [x for x in range(len(df)) if df.iloc[:, 78] == "FRQ"] 
    # num_count_list=[num_count_list.append(df.iloc[x, 3]) for x in range(len(df)) if df.iloc[x, 78] == "FRQ"]

    # result = num_count_list.count(num_count_list[0]) == len(num_count_list)
    # if (result):
    #     next_num = 1000
    # else:
    #     next_num = max(num_count_list)

    # for i in range(len(df)):
    #     identifier = df.iloc[i, 78]
    #     tag_part_3 = df.iloc[i, 3]
    #     if identifier == "FRQ" and pd.isna(df.iloc[i, 95]):
    #         next_num = next_num + 1
    #         df.iloc[i, 95] = str(next_num)  
    #         for x in range(len(df)):
    #             identifier = df.iloc[x, 78]
    #             if (identifier == "FRQ_Ptc") and (df.iloc[x, 3] == tag_part_3):
    #                 df.iloc[x, 95] = str(next_num)
    #             elif (identifier == "FRQ_Pro") and (df.iloc[x, 3] == tag_part_3):
    #                 df.iloc[x, 95] = str(next_num)
    #             elif (identifier == "FRQ_R") and (df.iloc[x, 3] == tag_part_3):
    #                 df.iloc[x, 95] = str(next_num)
    #             elif (identifier == "FRQ_Dis") and (df.iloc[x, 3] == tag_part_3):
    #                 df.iloc[x, 95] = str(next_num)
    #             elif (identifier == "FRQ_Rot") and (df.iloc[x, 3] == tag_part_3):
    #                 df.iloc[x, 95] = str(next_num)
    #                 break
generateCmNo()