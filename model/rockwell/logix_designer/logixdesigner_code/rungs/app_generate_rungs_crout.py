import pandas as pd
from lxml import etree

def getModuleCroutRungs(df, nr):
    # Get total number of rungs to create
    var_rungNr = 0
    var_rungCount = 0
    for x in range(len(df)):
        if (str(df.loc[x, "PLC No."]) == str(nr)):
            var_rungCount = var_rungCount+1
    var_rungCount = str(var_rungCount)

    RSLogix5000Content = etree.Element('RSLogix5000Content', SchemaRevision="1.0", SoftwareRevision="33.00", TargetType="Rung", TargetCount=var_rungCount, CurrentLanguage="en-US", ContainsContext="true", ExportDate="Fri Aug 20 11:38:35 2021", ExportOptions="References NoRawData L5KData DecoratedData Context RoutineLabels AliasExtras IOTags NoStringData ForceProtectedEncoding AllProjDocTrans")
    Controller = etree.SubElement(RSLogix5000Content, 'Controller', Use="Context", Name=f'PLC{nr}')
    Programs = etree.SubElement(Controller, 'Programs', Use="Context")
    Program = etree.SubElement(Programs, 'Program', Use="Context", Name="Safety_Z1")
    Tags = etree.SubElement(Program, 'Tags', Use='Context')
    Routines = etree.SubElement(Program, 'Routines', Use="Context")
    Routine = etree.SubElement(Routines, 'Routine', Use="Context", Name="R011_Output")
    RLLContent = etree.SubElement(Routine, 'RLLContent', Use="Context")

    # For loop to gather all relevant data for each row
    for i in range(len(df)):
        if (str(df.loc[i, "PLC No."]) == str(nr)):
            tag_name = f'{df.loc[i, "Tag"]}'
            tag_crout_aoi = f'{tag_name}_CROUT_AOI'
            tag_out = f'{df.loc[i, "Emergency Stop Contactor"]}'
            tag_fb = f'{df.loc[i, "Emergency Stop Contactor FB"]}_SP'
            tag_sf_ok = f'{tag_name}_SF_OK'
            tag_name_qe = tag_name
            tag_name_qe = tag_name_qe.replace("MA", "QE")
            tag_name_qe = tag_name_qe.replace("FC", "QE")
            tag_enable = f'{tag_name_qe}_Enable'
            plcAdressTmp = f'{df.loc[i, "Forward PLC address"]}'
            tag_plcAdress = plcAdressTmp.replace('Data', "")
            var_panelName = f'{df.loc[i, "Tag Part 2"]}'
            var_comment = f'{df.loc[i, "Description"]}'
            var_rungNr = var_rungNr+1
            
            Rung = etree.SubElement(RLLContent, 'Rung', Use="Target", Number=str(var_rungNr), Type="N")
            etree.SubElement(Rung, 'Comment').text = etree.CDATA(f'{var_panelName} - {var_comment}\n-------------------------------------o------------------------------------\n{tag_enable}\n{tag_fb}\n{tag_out}') # \n for new line
            etree.SubElement(Rung, 'Text').text = etree.CDATA(f'[CROUT({tag_crout_aoi},NEGATIVE,500,{tag_enable},{tag_fb},{tag_fb},ON_SP,{tag_plcAdress}OutputStatus,L_ResetOutputCircuit) ,XIC({tag_crout_aoi}.O1) OTE({tag_out}) OTE({tag_sf_ok}) ];')

    tree = etree.ElementTree(RSLogix5000Content)
    etree.indent(tree, space="")
    tree.write('export/rockwell/rungs/RA_RUNGS_CROUT.l5x', pretty_print=True, encoding="utf-8", xml_declaration=True)