import pandas as pd
from lxml import etree

def getModuleStsRungs(df, nr):

    # Get total number of rungs to create
    var_rungNr = 0
    var_rungCount = 0
    for x in range(len(df)):
        if (str(df.loc[x, "PLC No."]) == str(nr)):
            var_rungCount = var_rungCount+1
    var_rungCount = str(var_rungCount)

    seqNr = 10

    RSLogix5000Content = etree.Element('RSLogix5000Content', SchemaRevision="1.0", SoftwareRevision="33.00", TargetType="Rung", TargetCount=var_rungCount, CurrentLanguage="en-US", ContainsContext="true", ExportDate="Fri Aug 20 11:38:35 2021", ExportOptions="References NoRawData L5KData DecoratedData Context RoutineLabels AliasExtras IOTags NoStringData ForceProtectedEncoding AllProjDocTrans")
    Controller = etree.SubElement(RSLogix5000Content, 'Controller', Use="Context", Name=f'PLC{nr}')
    Programs = etree.SubElement(Controller, 'Programs', Use="Context")
    Program = etree.SubElement(Programs, 'Program', Use="Context", Name="IO")
    Tags = etree.SubElement(Program, 'Tags', Use='Context')
    Routines = etree.SubElement(Program, 'Routines', Use="Context")
    Routine = etree.SubElement(Routines, 'Routine', Use="Context", Name="R012_ModuleStatus")
    RLLContent = etree.SubElement(Routine, 'RLLContent', Use="Context")

    # For loop to gather all relevant data for each row
    for i in range(len(df)):
        if (str(df.loc[i, "PLC No."]) == str(nr)):
            tagPart2 = df.loc[i, "Tag Part 2"]
            tagPart2_noDot = tagPart2.split('.', 1)[0]
            tagPart3 = df.loc[i, "Tag Part 3"]
            tag_name = f'{df.loc[i, "Tag Name"]}.S.Comm_Status'
            var_panelName = f'{df.loc[i, "Tag Part 2"]}'
            var_comment = f'{df.loc[i, "Description"]}'
            f_moduleStatus = f'{tagPart2_noDot}_{tagPart3}_ModuleSts_AOI'
            in_entryStatus = f'{tagPart2_noDot}_{tagPart3}_EntrySts_Node'
            var_rungNr = var_rungNr+1
            ipAdr = df.loc[i, "IP-address"]
            seqNr = seqNr+1

            
            Rung = etree.SubElement(RLLContent, 'Rung', Use="Target", Number=str(var_rungNr), Type="N")
            etree.SubElement(Rung, 'Comment').text = etree.CDATA(f'{var_panelName} - {var_comment}\n-------------------------------------o------------------------------------\nGet Network Status of - {ipAdr}') # \n for new line
            etree.SubElement(Rung, 'Text').text = etree.CDATA(f'EQU(Eth2223_SeqStep,{seqNr})GSV(Module,{tagPart3},EntryStatus,{in_entryStatus})F_ModuleStatus({f_moduleStatus},{in_entryStatus},{tag_name});')

    tree = etree.ElementTree(RSLogix5000Content)
    etree.indent(tree, space="")
    tree.write('export/rockwell/rungs/RA_RUNGS_ModuleSts.l5x', pretty_print=True, encoding="utf-8", xml_declaration=True)