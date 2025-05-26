from ast import IsNot
import pandas as pd


def functionBlock(FBName, LibName, DbName, nr, df, dfTemplate):
    filename = "export/siemens/PLC_Logic/%s.awl" % FBName

    with open(filename, 'w') as f:
        L0 = str(len(df))

# TIA Logic Format (Fixed Text)
        L1 = []
        L1.append(str(f'FUNCTION_BLOCK "{FBName}"\n'))
        L1.append(str("TITLE = Control module\n"))
        L1.append(str("{ S7_Optimized_Access := 'TRUE' }\n"))
        L1.append(str("VERSION : 0.1\n"))
        L1.append(str(" VAR\n"))
        L1.append(str(" END_VAR\n"))
        L1.append(str("\n"))
        L1.append(str("\n"))
        L1.append(str(f'BEGIN\n'))

        f.writelines(L1)

        for i in range(len(df)):
            CM_dict = {}
            Tag = str(df.loc[i]["Tag"])
            Description = str(df.loc[i]["Description"])

            for j in range(len(dfTemplate)):    # Iterate Template df
                #print(j)
                obj = dfTemplate.loc[j]["Objects"]
                # Check worksheet column is not Null
                if not pd.isnull(dfTemplate.loc[j]["WorksheetColumnName"]):
                    # if Not Null then use this data as a column name to find value from main df
                    keyWorksheetCol = dfTemplate.loc[j]["WorksheetColumnName"]
                    # Check main df data value is not Null
                    if not pd.isnull(df.loc[i][keyWorksheetCol]):
                        # if Not Null Copy to dictionary
                        CM_dict[obj] = df.loc[i][keyWorksheetCol]
                    # else check on template df, if any Default Values present
                    elif not pd.isnull(dfTemplate.loc[j]["DefaultValues"]):
                        CM_dict[obj] = dfTemplate.loc[j]["DefaultValues"]
                    else:
                        CM_dict[obj] = ""
                # else check on template df, if any Default Values present
                elif not pd.isnull(dfTemplate.loc[j]["DefaultValues"]):
                    CM_dict[obj] = dfTemplate.loc[j]["DefaultValues"]
                else:
                    CM_dict[obj] = ""
            print(CM_dict)

# TIA Logic Format (Network)
            CM_No = (CM_dict.get('CM_No'))
            L2 = []

            L2.append(str("NETWORK\n"))
            L2.append(str(f'TITLE = {CM_No} - {Tag} - {Description}\n\n'))
            L2.append(str(f'       CALL #"{Tag}"\n'))
            L2.append(str("       (\n"))

            for k in range(len(dfTemplate)):
                obj = dfTemplate.loc[k]["Objects"]
                # finding CM_XXX object to assign array db for HMI Interface
                if obj == "CM_"+DbName:
                    L2.append(
                        str(f'         CM_{DbName}        := "dbPlcHmi{DbName}".{DbName}[{CM_No}] ,\n'))
                # finding null values in dataframe and assign nothing for those values
                elif CM_dict[obj] == "nan":
                    L2.append(str(f'         {obj}       := ' ' ,\n'))
                # generate rest of other objects and assign their values from dataframe
                elif CM_dict[obj] != "":
                    L2.append(
                        str(f'         {obj}       := {CM_dict[obj]} ,\n'))

            L2.append(str("       );\n\n"))

            f.writelines(L2)

# Create Static variables in the DB

    for i in range(len(df)):
        with open(filename, 'r') as f:
            contents = f.readlines()
            Tag = str(df.loc[i]["Tag"])
            L3 = f'   "{Tag}" : "{LibName}";\n'
            Line = 5+i  # insert after the first 5 lines
            contents.insert(Line, L3)

        with open(filename, "w") as f:
            contents = "".join(contents)
            f.write(contents)

# End FB
    with open(filename, 'a') as f:
        f.write("END_FUNCTION_BLOCK\n")
        f.close()
