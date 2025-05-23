import pandas as pd
from lxml import etree
from pandas.core.dtypes.missing import notna


def getFrqRungs(df, nr, emptyRungsCheckbox, Cmd_AlmDint):

    # Get total number of rungs to create
    var_rungNr = 0
    var_rungCount = 0
    for x in range(len(df)):
        if not pd.isna(df.loc[x, "Area"]) and (str(df.loc[x, "PLC No."]) == str(nr)):
            var_rungCount = var_rungCount+1
    var_rungCount = str(var_rungCount)

    RSLogix5000Content = etree.Element('RSLogix5000Content', SchemaRevision="1.0", SoftwareRevision="33.00", TargetType="Rung", TargetCount=var_rungCount, CurrentLanguage="en-US", ContainsContext="true", ExportDate="Fri Aug 20 11:38:35 2021", ExportOptions="References NoRawData L5KData DecoratedData Context RoutineLabels AliasExtras IOTags NoStringData ForceProtectedEncoding AllProjDocTrans")
    Controller = etree.SubElement(RSLogix5000Content, 'Controller', Use="Context", Name=f'PLC{nr}')
    Programs = etree.SubElement(Controller, 'Programs', Use="Context")
    Program = etree.SubElement(Programs, 'Program', Use="Context", Name="IO")
    Tags = etree.SubElement(Program, 'Tags', Use='Context')
    Routines = etree.SubElement(Program, 'Routines', Use="Context")
    Routine = etree.SubElement(Routines, 'Routine', Use="Context", Name="R042_FRQ")
    RLLContent = etree.SubElement(Routine, 'RLLContent', Use="Context")

    # For loop to gather all relevant data for each row
    for i in range(len(df)):
        if (str(df.loc[i, "PLC No."]) == str(nr)) and not emptyRungsCheckbox:
            var_panelName = f'{df.loc[i, "Cabinet"]}'
            var_comment = f'{df.loc[i, "Description"]}'
            tag_frq_udt = f'{df.loc[i, "Tag"]}_FRQ_UDT'
            tag_com_udt = f'{df.loc[i, "Tag"]}_COM_UDT'
            tag_com_f = f'{df.loc[i, "Tag"]}_COM_F'
            tag_cm_frq = f'{df.loc[i, "Tag"]}_FRQ_CM'
            tag_part3 = f'{df.loc[i, "Tag Part 3"]}'
            tag_inp_disconnect = f'{df.loc[i, "Disconnect"]}'
            tag_inp_thermal = f'{df.loc[i, "Thermal Fault"]}'
            if pd.notna(df.loc[i, "Rotation Sensor"]): tag_inp_rot = f'{df.loc[i, "Rotation Sensor"]}'
            else: tag_inp_rot = "Off"
            tag_l_safe = f'{df.loc[i, "Tag"]}_SafetyOK'
            var_tabId = f'{df.loc[i, "Tab ID"]}'
            var_subId = f'{df.loc[i, "Sub ID"]}'
            var_sectionLocal = f'{df.loc[i, "SC Local"]}'
            frq_type = f'{df.loc[i, "FRQ Type"]}'
            var_rungNr = var_rungNr+1
            var_EU = df.loc[i, "EU"]
            euMin = df.loc[i, "Min EU"]
            euMax = df.loc[i, "Max EU"]
            rawMin = df.loc[i, "Raw Min"]
            rawMax = df.loc[i, "Raw Max"]
            var_ipadr = df.loc[i, "IP Address"]
            var_almDint = f'{df.loc[i, "Tag"]}_ALM_DINT'

            #Generates rung with relevant information for each frequency inverter
            Rung = etree.SubElement(RLLContent, 'Rung', Use="Target", Number=str(var_rungNr), Type="N")
            etree.SubElement(Rung, 'Comment').text = etree.CDATA(f'{var_panelName}\n----------0----------\n{var_comment}\nIP-address: {var_ipadr}\nDisconnect: {tag_inp_disconnect}\nThermal: {tag_inp_thermal}\nRotation: {tag_inp_rot}\nFRQ_UDT: {tag_frq_udt}\nCOM_UDT: {tag_com_udt}\nCOM_F: {tag_com_f}\nFRQ_CM: {tag_cm_frq}\nEU: {var_EU}\nEU min-max: {euMin} - {euMax}\nRAW min-max: {rawMin} - {rawMax}\nFRQ Type: {frq_type}\nTab ID: {var_tabId}\nSub ID: {var_subId}\nSection Local: {var_sectionLocal}\n') # \n for new line
            etree.SubElement(Rung, 'Text').text = etree.CDATA(f'NOP();')

            var_rungNr = var_rungNr+1
            # Generates rungs for frequency inverters
            Rung = etree.SubElement(RLLContent, 'Rung', Use="Target", Number=str(var_rungNr), Type="N")
            etree.SubElement(Rung, 'Comment').text = etree.CDATA(f'{var_panelName}\n----------0----------\n{var_comment}\n') # \n for new line
            if Cmd_AlmDint:
                etree.SubElement(Rung, 'Text').text = etree.CDATA(f'CM_FRQ({tag_cm_frq},PLANT,{var_sectionLocal},DisplayNames,{tag_l_safe},{tag_inp_disconnect},{tag_inp_thermal},{tag_inp_rot},On,Off,{tag_cm_frq}.Inp_Speed,{tag_frq_udt},{tag_com_udt},{var_tabId},{var_subId},{var_almDint}) F_{frq_type}({tag_com_f},{tag_com_udt},{tag_part3},Axes,{tag_frq_udt}.S.Comm_Status);')
            else:
                etree.SubElement(Rung, 'Text').text = etree.CDATA(f'CM_FRQ({tag_cm_frq},PLANT,{var_sectionLocal},DisplayNames,{tag_l_safe},{tag_inp_disconnect},{tag_inp_thermal},{tag_inp_rot},On,Off,{tag_cm_frq}.Inp_Speed,{tag_frq_udt},{tag_com_udt},{var_tabId},{var_subId}) F_{frq_type}({tag_com_f},{tag_com_udt},{tag_part3},Axes,{tag_frq_udt}.S.Comm_Status);')

        elif (str(df.loc[i, "PLC No."]) == str(nr)) and emptyRungsCheckbox:
            var_panelName = f'{df.loc[i, "Cabinet"]}'
            var_comment = f'{df.loc[i, "Description"]}'
            var_ipadr = df.loc[i, "IP Address"]
            var_rungNr = var_rungNr+1
            tag_inp_disconnect = f'{df.loc[i, "Disconnect"]}'
            tag_inp_thermal = f'{df.loc[i, "Thermal Fault"]}'
            if pd.notna(df.loc[i, "Rotation Sensor"]): tag_inp_rot = f'{df.loc[i, "Rotation Sensor"]}'
            else: tag_inp_rot = "Not in use"
            var_EU = df.loc[i, "EU"]
            euMin = df.loc[i, "Min EU"]
            euMax = df.loc[i, "Max EU"]
            rawMin = df.loc[i, "Raw Min"]
            rawMax = df.loc[i, "Raw Max"]
            frq_type = f'{df.loc[i, "FRQ Type"]}'
            var_tabId = f'{df.loc[i, "Tab ID"]}'
            var_subId = f'{df.loc[i, "Sub ID"]}'
            var_sectionLocal = f'{df.loc[i, "SC Local"]}'
            tag_frq_udt = f'{df.loc[i, "Tag"]}_FRQ_UDT'
            tag_com_udt = f'{df.loc[i, "Tag"]}_COM_UDT'
            tag_com_f = f'{df.loc[i, "Tag"]}_COM_F'
            tag_cm_frq = f'{df.loc[i, "Tag"]}_FRQ_CM'
            
            #Generates rung with relevant information for each frequency inverter
            Rung = etree.SubElement(RLLContent, 'Rung', Use="Target", Number=str(var_rungNr), Type="N")
            etree.SubElement(Rung, 'Comment').text = etree.CDATA(f'{var_panelName}\n----------0----------\n{var_comment}\nIP-address: {var_ipadr}\nDisconnect: {tag_inp_disconnect}\nThermal: {tag_inp_thermal}\nRotation: {tag_inp_rot}\nFRQ_UDT: {tag_frq_udt}\nCOM_UDT: {tag_com_udt}\nCOM_F: {tag_com_f}\nFRQ_CM: {tag_cm_frq}\nEU: {var_EU}\nEU min-max: {euMin} - {euMax}\nRAW min-max: {rawMin} - {rawMax}\nFRQ Type: {frq_type}\nTab ID: {var_tabId}\nSub ID: {var_subId}\nSection Local: {var_sectionLocal}\n') # \n for new line
            etree.SubElement(Rung, 'Text').text = etree.CDATA(f'NOP();')

            var_rungNr = var_rungNr+1
            # Generates rungs for frequency inverters
            Rung = etree.SubElement(RLLContent, 'Rung', Use="Target", Number=str(var_rungNr), Type="N")
            etree.SubElement(Rung, 'Comment').text = etree.CDATA(f'{var_panelName}\n----------0----------\n{var_comment}\n') # \n for new line
            etree.SubElement(Rung, 'Text').text = etree.CDATA(f'NOP();')

            

    tree = etree.ElementTree(RSLogix5000Content)
    etree.indent(tree, space="")
    tree.write('export/rockwell/rungs/RA_RUNGS_FRQ.l5x', pretty_print=True, encoding="utf-8", xml_declaration=True)