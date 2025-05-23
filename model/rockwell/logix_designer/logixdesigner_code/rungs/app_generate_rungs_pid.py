import pandas as pd
from lxml import etree

def getPidRungs(df, nr, Cmd_AlmDint):
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
    Routine = etree.SubElement(Routines, 'Routine', Use="Context", Name="R060_PID")
    RLLContent = etree.SubElement(Routine, 'RLLContent', Use="Context")

    # For loop to gather all relevant data for each row
    for i in range(len(df)):
        if (str(df.loc[i, "PLC No."]) == str(nr)):
            no_dot_name = f'{df.loc[i, "Tag"]}'
            var_panelName = f'{df.loc[i, "Cabinet"]}'
            var_comment = f'{df.loc[i, "Description"]}'
            tag_pid_udt = f'{no_dot_name}_PID_UDT'
            tag_cm_pid = f'{no_dot_name}_PID_CM'
            cm_cv_out = f'{tag_cm_pid}.Out_CV'
            var_tabId = f'{df.loc[i, "Tab ID"]}'
            var_subId = f'{df.loc[i, "Sub ID"]}'
            var_sectionLocal = f'{df.loc[i, "SC Local"]}'
            var_almDint = f'{df.loc[i, "Tag"]}_ALM_DINT'
            var_rungNr = var_rungNr+1

            
            Rung = etree.SubElement(RLLContent, 'Rung', Use="Target", Number=str(var_rungNr), Type="N")
            etree.SubElement(Rung, 'Comment').text = etree.CDATA(f'{var_panelName}\n----------0----------\n{var_comment}\n') # \n for new line
            if Cmd_AlmDint:
                etree.SubElement(Rung, 'Text').text = etree.CDATA(f'CM_PID({tag_cm_pid},PLANT,{var_sectionLocal},DisplayNames,0,0.0,1000,0.0,{tag_pid_udt},{var_tabId},{var_subId},{cm_cv_out},{var_almDint});')
            else:
                etree.SubElement(Rung, 'Text').text = etree.CDATA(f'CM_PID({tag_cm_pid},PLANT,{var_sectionLocal},DisplayNames,0,0.0,1000,0.0,{tag_pid_udt},{var_tabId},{var_subId},{cm_cv_out});')

    tree = etree.ElementTree(RSLogix5000Content)
    etree.indent(tree, space="")
    tree.write('export/rockwell/rungs/RA_RUNGS_PID.l5x', pretty_print=True, encoding="utf-8", xml_declaration=True)