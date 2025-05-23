import pandas as pd
from lxml import etree

def getSfMapRungs(df_import3): #Use "Safety Mapping - Template" as import


    df_io = df_import3.copy()
    df_io = pd.DataFrame(df_import3.iloc[1:, :])
    df = df_io.copy()

    # Get total number of rungs to create
    var_rungNr = 0
    var_rungCount = 0

    for x in range(len(df)):
        if not pd.isna(df.loc[x, "Tag name to be safety mapped:"]):     
            var_rungCount = var_rungCount+1
    var_rungCount = str(var_rungCount)

    RSLogix5000Content = etree.Element('RSLogix5000Content', SchemaRevision="1.0", SoftwareRevision="33.00", TargetType="Rung", TargetCount=var_rungCount, CurrentLanguage="en-US", ContainsContext="true", ExportDate="Fri Aug 20 11:38:35 2021", ExportOptions="References NoRawData L5KData DecoratedData Context RoutineLabels AliasExtras IOTags NoStringData ForceProtectedEncoding AllProjDocTrans")
    Controller = etree.SubElement(RSLogix5000Content, 'Controller', Use="Context", Name="PLC1")
    Programs = etree.SubElement(Controller, 'Programs', Use="Context")
    Program = etree.SubElement(Programs, 'Program', Use="Context", Name="IO")
    Tags = etree.SubElement(Program, 'Tags', Use='Context')
    Routines = etree.SubElement(Program, 'Routines', Use="Context")
    Routine = etree.SubElement(Routines, 'Routine', Use="Context", Name="R034_AIN")
    RLLContent = etree.SubElement(Routine, 'RLLContent', Use="Context")

    # For loop to gather all relevant data for each row
    for i in range(len(df)):
        tag_name = f'{df.loc[i, "Tag name to be safety mapped:"]}'
        tag_name_list = list(tag_name) # Remove the . in the tag name
        if tag_name_list[4] == ('.'):
            tag_name_list[4] = ''
            tag_name_list[5] = ''
        elif tag_name_list[5] == ('.'):
            tag_name_list[5] = ''
            tag_name_list[6] = ''
        no_dot_name = "".join(tag_name_list) # to here
        s_tag = f'{no_dot_name}'
        sp_tag = f'{no_dot_name}_S'
        comment = f'{df.loc[i, "Description:"]}'
  
        
        Rung = etree.SubElement(RLLContent, 'Rung', Use="Target", Number=str(var_rungNr), Type="N")
        etree.SubElement(Rung, 'Comment').text = etree.CDATA(f'{comment}') # \n for new line
        etree.SubElement(Rung, 'Text').text = etree.CDATA(f'XIC({s_tag})OTE({sp_tag});')
 
    tree = etree.ElementTree(RSLogix5000Content)
    etree.indent(tree, space="")
    tree.write('export/rockwell/rungs/RA_RUNGS_SafeMap.l5x', pretty_print=True, encoding="utf-8", xml_declaration=True)