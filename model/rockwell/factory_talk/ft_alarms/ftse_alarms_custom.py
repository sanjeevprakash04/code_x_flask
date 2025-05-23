import pandas as pd
from lxml import etree

def getFTSEAlarmsCustom(df_import1):

    df_io = df_import1.copy()
    df_io = pd.DataFrame(df_import1.iloc[2:, :])
    df = df_io.copy()


    print(df)
    # Adds prefix to attributes
    FTAeAlarmStore_name = etree.QName("http://www.w3.org/2001/XMLSchema-instance", "schemaLocation")
    nsmap = {"dt": "urn:schemas-microsoft-com:datatypes",
         None: "urn://www.factorytalk.net/schema/2003/FTLDDAlarms.xsd",
         "xsi": "http://www.w3.org/2001/XMLSchema-instance"}
    FTAeAlarmStore = etree.Element("FTAeAlarmStore", {FTAeAlarmStore_name: "urn://www.factorytalk.net/schema/2003/FTLDDAlarms.xsd FTLDDAlarms.xsd"}, nsmap=nsmap)

    etree.SubElement(FTAeAlarmStore, 'Version').text = "11.0.0"
    Commands = etree.SubElement(FTAeAlarmStore, 'Commands')
    FTAeDetectorCommand = etree.SubElement(Commands, 'FTAeDetectorCommand')
    etree.SubElement(FTAeDetectorCommand, 'Operation').text = "SetLanguages"

    # Adds the xml prefix to the lang attribute
    class XMLNamespaces:
        xml = "http://www.w3.org/XML/1998/namespace"
    etree.SubElement(FTAeDetectorCommand, "Language",{etree.QName(XMLNamespaces.xml, "lang"): "en-US"})

    FTAeDetectorCommand = etree.SubElement(Commands, 'FTAeDetectorCommand', style="FTAeDefaultDetector", version="11.0.0")
    etree.SubElement(FTAeDetectorCommand, 'Operation').text = "SetDAPollGroups"
    PollGroups = etree.SubElement(FTAeDetectorCommand, 'PollGroups')
    etree.SubElement(PollGroups, 'PollGroupTags', rate="0.10").text = ""
    etree.SubElement(PollGroups, 'PollGroupTags', rate="0.25").text = ""
    etree.SubElement(PollGroups, 'PollGroupTags', rate="0.50").text = ""
    etree.SubElement(PollGroups, 'PollGroupTags', rate="1").text = ""
    PollGroupTags = etree.SubElement(PollGroups, 'PollGroupTags', rate="2")

    # Create alarm tags
    for i in range(len(df)):
        tag_name = df.iloc[i, 0]
        plcNr = df.iloc[i, 3]
        etree.SubElement(PollGroupTags, 'Tag').text = f'[plc{plcNr}]{tag_name}'
    
    etree.SubElement(PollGroups, 'PollGroupTags', rate="5").text = ""
    etree.SubElement(PollGroups, 'PollGroupTags', rate="10").text = ""
    etree.SubElement(PollGroups, 'PollGroupTags', rate="20").text = ""
    etree.SubElement(PollGroups, 'PollGroupTags', rate="30").text = ""
    etree.SubElement(PollGroups, 'PollGroupTags', rate="60").text = ""
    etree.SubElement(PollGroups, 'PollGroupTags', rate="120").text = ""

    FTAeDetectorCommand = etree.SubElement(Commands, 'FTAeDetectorCommand', style="FTAeDefaultDetector", version="11.0.0")
    etree.SubElement(FTAeDetectorCommand, 'Operation').text = "WriteMsg"
    Messages = etree.SubElement(FTAeDetectorCommand, 'Messages')

    # Create alarm messages
    for i in range(len(df)):
        msgid = df.iloc[i, 4]
        msgid = str(msgid).zfill(5) # Makes number always be 5 digits long
        description = df.iloc[i, 2]
        tag_name_mes = f'({df.iloc[i, 1]})'
        Message = etree.SubElement(Messages, 'Message', id = str(msgid))
        Msgs = etree.SubElement(Message, 'Msgs')
        etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'{description} - {tag_name_mes}'

    FTAeDetectorCommand = etree.SubElement(Commands, 'FTAeDetectorCommand', style="FTAeDefaultDetector", version="11.0.0")
    etree.SubElement(FTAeDetectorCommand, 'Operation').text = "WriteConfig"
    FTAlarmElements = etree.SubElement(FTAeDetectorCommand, 'FTAlarmElements', shelveMaxValue="480")

    for i in range(len(df)):
        tag_name = df.iloc[i, 0]
        severity = f'{df.iloc[i, 5]}'
        plcNr = df.iloc[i, 3]
        msgid = df.iloc[i, 4]
        msgid = str(msgid).zfill(5) # Makes number always be 5 digits long
        FTAlarmElement = etree.SubElement(FTAlarmElements, 'FTAlarmElement', name=f'{msgid} Alarm', latched="false", ackRequired="true", style="Discrete")
        DiscreteElement = etree.SubElement(FTAlarmElement, 'DiscreteElement')
        etree.SubElement(DiscreteElement, 'DataItem').text = f'{tag_name}'
        etree.SubElement(DiscreteElement, 'Style').text = "DiscreteTrue"
        etree.SubElement(DiscreteElement, 'Severity').text = severity
        etree.SubElement(DiscreteElement, 'DelayInterval').text = "0"
        etree.SubElement(DiscreteElement, 'EnableTag').text = "false"
        etree.SubElement(DiscreteElement, 'UserData')
        etree.SubElement(DiscreteElement, 'RSVCmd').text = ""
        etree.SubElement(DiscreteElement, 'AlarmClass')
        etree.SubElement(DiscreteElement, 'GroupID').text = "0"
        HandshakeTags = etree.SubElement(DiscreteElement, 'HandshakeTags')
        etree.SubElement(HandshakeTags, 'InAlarmDataItem').text = ""
        etree.SubElement(HandshakeTags, 'DisabledDataItem').text = ""
        etree.SubElement(HandshakeTags, 'AckedDataItem').text = ""
        etree.SubElement(HandshakeTags, 'SuppressedDataItem').text = ""
        etree.SubElement(HandshakeTags, 'ShelvedDataItem').text = ""
        etree.SubElement(DiscreteElement, 'RemoteAckAllDataItem', AutoReset="false").text = ""
        etree.SubElement(DiscreteElement, 'RemoteDisableDataItem', AutoReset="false").text = ""
        etree.SubElement(DiscreteElement, 'RemoteEnableDataItem', AutoReset="false").text = ""
        etree.SubElement(DiscreteElement, 'RemoteSuppressDataItem', AutoReset="false").text = ""
        etree.SubElement(DiscreteElement, 'RemoteUnSuppressDataItem', AutoReset="false").text = ""
        etree.SubElement(DiscreteElement, 'RemoteShelveAllDataItem', AutoReset="false").text = ""
        etree.SubElement(DiscreteElement, 'RemoteUnShelveDataItem', AutoReset="false").text = ""
        etree.SubElement(DiscreteElement, 'RemoteShelveDuration').text = ""
        etree.SubElement(DiscreteElement, 'MessageID').text = str(msgid)
        etree.SubElement(DiscreteElement, 'Params').text = ""



    tree = etree.ElementTree(FTAeAlarmStore)
    etree.indent(tree, space="")
    tree.write('export/rockwell/ftseAlarms/RA_FTSEAlarms_Custom.xml', pretty_print=True, encoding="utf-8", xml_declaration=True)
