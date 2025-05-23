import pandas as pd
from lxml import etree

def getMtrRungs(df, nr, Cmd_AlmDint):
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
    Routine = etree.SubElement(Routines, 'Routine', Use="Context", Name="R040_MTR")
    RLLContent = etree.SubElement(Routine, 'RLLContent', Use="Context")

    # For loop to gather all relevant data for each row
    for i in range(len(df)):
        if (str(df.loc[i, "PLC No."]) == str(nr)):
            no_dot_name = f'{df.loc[i, "Tag"]}'
            no_dot_name_qe = no_dot_name.replace("MA", "QE")
            var_panelName = f'{df.loc[i, "Cabinet"]}'
            var_comment = f'{df.loc[i, "Description"]}'
            tag_mtr_udt = f'{no_dot_name}_MTR_UDT'
            tag_cm_mtr = f'{no_dot_name}_MTR_CM'
            tag_inp_disconnect = f'{df.loc[i, "Disconnect"]}'
            tag_inp_thermal = f'{df.loc[i, "Thermal Fault"]}'
            tag_l_safe = f'{no_dot_name}_SafetyOK'
            tag_sf_ok = f'{no_dot_name}_SF_OK'
            tag_safe_fp = f'\Safety_Z1.{no_dot_name_qe}_CROUT_AOI.FP'
            if pd.notna(df.loc[i, "Forward Feedback"]): tag_inp_fb_fwd = f'{df.loc[i, "Forward Feedback"]}'
            else: tag_inp_fb_fwd = "Off"
            if pd.notna(df.loc[i, "Reverse Feedback"]): tag_inp_fb_rev = f'{df.loc[i, "Reverse Feedback"]}'
            else: tag_inp_fb_rev = "Off"
            if pd.notna(df.loc[i, "Start Forward"]): tag_out_fwd = f'{df.loc[i, "Start Forward"]}_S'
            else: tag_out_fwd = "Dummy_Out_P"
            if pd.notna(df.loc[i, "Start Reverse"]): tag_out_rev = f'{df.loc[i, "Start Reverse"]}_S'
            else: tag_out_rev = "Dummy_Out_N"
            var_tabId = f'{df.loc[i, "Tab ID"]}'
            var_subId = f'{df.loc[i, "Sub ID"]}'
            var_sectionLocal = f'{df.loc[i, "SC Local"]}'
            var_almDint = f'{df.loc[i, "Tag"]}_ALM_DINT'
            var_rungNr = var_rungNr+1

            
            Rung = etree.SubElement(RLLContent, 'Rung', Use="Target", Number=str(var_rungNr), Type="N")
            etree.SubElement(Rung, 'Comment').text = etree.CDATA(f'{var_panelName}\n----------0----------\n{var_comment}\n') # \n for new line
            #etree.SubElement(Rung, 'Text').text = etree.CDATA(f'CM_MTR({tag_cm_mtr},PLANT,{var_sectionLocal},DisplayNames,{tag_l_safe},{tag_safe_fp},{tag_inp_disconnect},{tag_inp_thermal},{tag_inp_fb_fwd},{tag_inp_fb_rev},{tag_mtr_udt},{var_tabId},{var_subId},{tag_out_fwd},{tag_out_rev});')
            if Cmd_AlmDint:
                etree.SubElement(Rung, 'Text').text = etree.CDATA(f'[XIO(MCC7_MCC7_QA0007_ALM_UDT.E.Alm) XIC(Zone1_OK) XIC(\Safety_Z1.{tag_sf_ok}) OTE({tag_l_safe}) ,CM_MTR({tag_cm_mtr},PLANT,{var_sectionLocal},DisplayNames,{tag_l_safe},{tag_safe_fp},{tag_inp_disconnect},{tag_inp_thermal},{tag_inp_fb_fwd},{tag_inp_fb_rev},{tag_mtr_udt},{var_tabId},{var_subId},{tag_out_fwd},{tag_out_rev},{var_almDint})];')
            else:
                etree.SubElement(Rung, 'Text').text = etree.CDATA(f'[XIO(MCC7_MCC7_QA0007_ALM_UDT.E.Alm) XIC(Zone1_OK) XIC(\Safety_Z1.{tag_sf_ok}) OTE({tag_l_safe}) ,CM_MTR({tag_cm_mtr},PLANT,{var_sectionLocal},DisplayNames,{tag_l_safe},{tag_safe_fp},{tag_inp_disconnect},{tag_inp_thermal},{tag_inp_fb_fwd},{tag_inp_fb_rev},{tag_mtr_udt},{var_tabId},{var_subId},{tag_out_fwd},{tag_out_rev})];')

    tree = etree.ElementTree(RSLogix5000Content)
    etree.indent(tree, space="")
    tree.write('export/rockwell/rungs/RA_RUNGS_MTR.l5x', pretty_print=True, encoding="utf-8", xml_declaration=True)