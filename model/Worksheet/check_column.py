import pandas as pd

def check_column_names(df, column_state):

    # Initialization of Dataframe   
    df.columns = df.iloc[2].astype(str) # Set the header to be at index 2
    df = pd.DataFrame(df.iloc[2:]) # Remove the first 3 rows and the first column
    df = df.reset_index()

    #List of State for every column names
    text_state = [False]*50

    #List of column names that must be in IO-list
    col_text = ["",
                "Sort",
                "TAG Part 1 (# System)",
                "TAG Part 2 (# Item)",
                "TAG Part 3 (Function code)",
                "TAG Part 4 (# Function serial)",
                "Component Description",
                "Process Description",
                "Generator Function",
                "CM No",
                "Tab ID",
                "Sub ID",
                "SC Local",
                "Main Power [kW]",
                "Main Current [A]",
                "Main Voltage [V]",
                "Control Current [A] OR [Nm] or (Connection)",
                "Poles",
                "Frequency [Hz]",
                "Cos φ (Efficiency)",
                "RPM",
                "EU",
                "Min EU",
                "Max EU",
                "Raw Min",
                "Raw Max",
                "PLC No",
                "PLC Tag Name",
                "PLC Address",
                "Net number / IP address",
                "FRQ Type",
                "VLV button P-Activate text",
                "VLV button N-DeAct text",
                "Component Type (Order number)",
                "Slice number",
                "Point",
                "Signal Type",
                "PLC Function",
                "PLC Bit address",
                "IO Address"
                ]

    #Check for column names in IO-list
    for x in range(len(col_text)):
        for i in range(len(df.columns)):              
            if df.iloc[0, i] == col_text[x]:
                text_state[x] = True

    #State 0 not in use
    text_state[0] = True 

    #Transfer missing column names to column state list for print
    for i in range(len(col_text)):
        if not text_state[i]:
            column_state[i] = col_text[i]