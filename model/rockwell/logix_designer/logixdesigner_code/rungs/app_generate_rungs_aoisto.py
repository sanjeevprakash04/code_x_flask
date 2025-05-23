import pandas as pd
from lxml import etree

def getAoiStoRungs(df, nr):
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
    Routine = etree.SubElement(Routines, 'Routine', Use="Context", Name="R011_OutputDrives")
    RLLContent = etree.SubElement(Routine, 'RLLContent', Use="Context")

    # For loop to gather all relevant data for each row
    for i in range(len(df)):
        if (str(df.loc[i, "PLC No."]) == str(nr)):
            tagPart3 = df.loc[i, "Tag Part 3"]
            tag_sto_aoi = f'{df.loc[i, "Tag"]}_STO_AOI'
            tag_sf_ok = f'{df.loc[i, "Tag"]}_SF_OK'
            frq_type = f'{df.loc[i, "FRQ Type"]}'
            var_rungNr = var_rungNr+1
            
            Rung = etree.SubElement(RLLContent, 'Rung', Use="Target", Number=str(var_rungNr), Type="N")
            etree.SubElement(Rung, 'Comment').text = etree.CDATA(f'{tagPart3} - STO\n----------0----------\n{frq_type} with Integrated Safe Torque-off') # \n for new line
            etree.SubElement(Rung, 'Text').text = etree.CDATA(f'[AOI_STO_V1_01({tag_sto_aoi},{tagPart3}:SI,{tagPart3}:SO,L_SF_Enable_AXES_STO,L_ResetOutputCircuit) ,XIC({tag_sto_aoi}.In_Enable) [XIO({tag_sto_aoi}.O1) XIO({tag_sto_aoi}.FP) OTL(L_FRQ_SO_Fault) ,XIC({tag_sto_aoi}.O1) OTE({tag_sf_ok}) ] ];')

    tree = etree.ElementTree(RSLogix5000Content)
    etree.indent(tree, space="")
    tree.write('export/rockwell/rungs/RA_RUNGS_STO_AOI.l5x', pretty_print=True, encoding="utf-8", xml_declaration=True)