import pandas as pd
from lxml import etree

df = pd.read_excel(r'export\worksheet\RA_Worksheet.xlsx', "DIN", dtype=str)

RSLogix5000Content = etree.Element('RSLogix5000Content', SchemaRevision="1.0", SoftwareRevision="33.00", TargetName="R020_ALM_TEST", TargetType="Routine", TargetSubType="RLL", ContainsContext="true", ExportDate="Thu Aug 12 17:06:13 2021", ExportOptions="References NoRawData L5KData DecoratedData Context Dependencies ForceProtectedEncoding AllProjDocTrans")
Controller = etree.SubElement(RSLogix5000Content, 'Controller', Use="Context", Name="FS121_PLC1_Main_00")
Programs = etree.SubElement(Controller, 'Programs', Use="Context")
Program = etree.SubElement(Programs, 'Program', Use="Context", Name="IO")
Tags = etree.SubElement(Program, 'Tags', Use='Context')
Routines = etree.SubElement(Program, 'Routines', Use="Context")
RoutineAlm = etree.SubElement(Routines, 'Routine', Use="Target", Name="R020_ALM", Type="RLL")
RLLContentAlm = etree.SubElement(RoutineAlm, 'RLLContent')
RoutineMes = etree.SubElement(Routines, 'Routine', Use="Target", Name="R019_MES", Type="RLL")
RLLContentMes = etree.SubElement(RoutineMes, 'RLLContent')
var_rungNr = 0

# Import of rungs for alarms
for i in range(len(df)):
    if f'{df.iloc[i, 4]}' != "Mes":
        tag_name = f'{df.iloc[i, 9]}_{df.iloc[i, 10]}_{df.iloc[i, 11]}'
        tag_name_list = list(tag_name) # Remove the . in the tag name
        if tag_name_list[4] == ('.'):
            tag_name_list[4] = ''
            tag_name_list[5] = ''
        elif tag_name_list[5] == ('.'):
            tag_name_list[5] = ''
            tag_name_list[6] = ''
        no_dot_name = "".join(tag_name_list) # to here
        var_panelName = f'{df.iloc[i, 4]}'
        var_comment = f'{df.iloc[i, 1]}'
        tag_alm_udt_e = f'{no_dot_name}_ALM_UDT.E.Alm'
        tag_alm_udt = f'{no_dot_name}_ALM_UDT'
        tag_alm_dint = f'{no_dot_name}_ALM_DINT'
        tag_cm_alm = f'{no_dot_name}_ALM_CM'
        tag_plc_name = f'{df.iloc[i, 8]}'
        var_tabId = f'{df.iloc[i, 5]}'
        var_subId = f'{df.iloc[i, 6]}'
        var_sectionLocal = f'SL_13' # Replace once placed in IO-List
        var_rungNr = str(i+1)

        # Generates rung for 'Mes' alarms, with reporting to 'Cabinet Fault' - is placed in R020_ALM routine
        Rung = etree.SubElement(RLLContentAlm, 'Rung', Number=var_rungNr, Type="N")
        etree.SubElement(Rung, 'Comment').text = etree.CDATA(f'{var_panelName}\n----------0----------\n{var_comment}\n') # \n for new line
        etree.SubElement(Rung, 'Text').text = etree.CDATA(f'[XIC({tag_alm_udt_e}) OTL(Cabinet_Fault_{var_panelName}) ,CM_ALM({tag_cm_alm},PLANT,{var_sectionLocal},DisplayNames,{tag_plc_name},{tag_alm_udt},{var_tabId},{var_subId},{tag_alm_dint}) ];')

    elif f'{df.iloc[i, 4]}' == "Mes":
        tag_name = f'{df.iloc[i, 9]}_{df.iloc[i, 10]}_{df.iloc[i, 11]}'
        tag_name_list = list(tag_name) # Remove the . in the tag name
        if tag_name_list[4] == ('.'):
            tag_name_list[4] = ''
            tag_name_list[5] = ''
        elif tag_name_list[5] == ('.'):
            tag_name_list[5] = ''
            tag_name_list[6] = ''
        no_dot_name = "".join(tag_name_list) # to here
        var_panelName = f'{df.iloc[i, 4]}'
        var_comment = f'{df.iloc[i, 1]}'
        tag_alm_udt_e = f'{no_dot_name}_ALM_UDT.E.Alm'
        tag_alm_udt = f'{no_dot_name}_ALM_UDT'
        tag_alm_dint = f'{no_dot_name}_ALM_DINT'
        tag_cm_alm = f'{no_dot_name}_ALM_CM'
        tag_plc_name = f'{df.iloc[i, 8]}'
        var_tabId = f'{df.iloc[i, 5]}'
        var_subId = f'{df.iloc[i, 6]}'
        var_sectionLocal = f'SL_13' # Replace once placed in IO-List
        var_rungNr = str(i+1)
    
        # Generates rung for 'Mes' alarms, without reporting to 'Cabinet Fault' - is placed in R019_MES routine
        Rung = etree.SubElement(RLLContentMes, 'Rung', Number=var_rungNr, Type="N")
        etree.SubElement(Rung, 'Comment').text = etree.CDATA(f'{var_panelName}\n----------0----------\n{var_comment}\n') # \n for new line
        etree.SubElement(Rung, 'Text').text = etree.CDATA(f'CM_ALM({tag_cm_alm},PLANT,{var_sectionLocal},DisplayNames,{tag_plc_name},{tag_alm_udt},{var_tabId},{var_subId},{tag_alm_dint});')
        

tree = etree.ElementTree(RSLogix5000Content)
etree.indent(tree, space="")
tree.write('export/rockwell/routine/RA_Routine_ALM.l5x', pretty_print=True, encoding="utf-8", xml_declaration=True)