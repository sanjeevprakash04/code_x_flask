import pandas as pd
from lxml import etree

def getFTSEAlarms(df, AlmNr):
    
    frq_alarm_types = [{'fault' : "Man", 'sev' : "251"}, {'fault' : "Ignore", 'sev' : "251"}, {'fault' : "Safety_Flt", 'sev' : "501"}, {'fault' : "Amp_H", 'sev' : "251"}, {'fault' : "Torq_H", 'sev' : "251"}, {'fault' : "Motor_Protect", 'sev' : "501"}, {'fault' : "Disconnect", 'sev' : "501"}, {'fault' : "Ptc_Flt", 'sev' : "501"}, {'fault' : "Run_FB", 'sev' : "501"}, {'fault' : "Rot_FB", 'sev' : "501"}, {'fault' : "Drive_Flt", 'sev' : "501"}, {'fault' : "Comm_Flt", 'sev' : "501"}, {'fault' : "Instruction_Flt", 'sev' : "501"}, {'fault' : "Power_Flt", 'sev' : "501"}, {'fault' : "Thermal_Flt", 'sev' : "501"}, {'fault' : "Position_Flt", 'sev' : "501"}, {'fault' : "Feedback_Flt", 'sev' : "501"}, {'fault' : "Overload_Flt", 'sev' : "501"}, {'fault' : "Amp_HH", 'sev' : "501"}, {'fault' : "Torq_HH", 'sev' : "501"}, {'fault' : "BrakeResistor_Flt", 'sev' : "501"}]
    mtr_alarm_types = [{'fault' : "Man", 'sev' : "251"}, {'fault' : "Ignore", 'sev' : "251"}, {'fault' : "Motor_Protect", 'sev' : "501"}, {'fault' : "Disconnect", 'sev' : "501"}, {'fault' : "Estop", 'sev' : "501"}, {'fault' : "Run_FB", 'sev' : "501"}, {'fault' : "Rot_FB", 'sev' : "501"}, {'fault' : "Run_Rev_FB", 'sev' : "501"}, {'fault' : "Safety_FP", 'sev' : "501"}]
    ain_alarm_types = [{'fault' : "Man", 'sev' : "251"}, {'fault' : "Ignore", 'sev' : "251"}, {'fault' : "LL", 'sev' : "501"}, {'fault' : "L", 'sev' : "251"}, {'fault' : "H", 'sev' : "251"}, {'fault' : "HH", 'sev' : "501"}, {'fault' : "Overflow", 'sev' : "501"}, {'fault' : "Underflow", 'sev' : "501"}]
    aout_alarm_types = [{'fault' : "Man", 'sev' : "251"}, {'fault' : "Ignore", 'sev' : "251"}, {'fault' : "Alm", 'sev' : "501"}, {'fault' : "Warning", 'sev' : "251"}, {'fault' : "SPAndPVError", 'sev' : "501"}]
    din_alarm_types = [{'fault' : "Man", 'sev' : "251"}, {'fault' : "Ignore", 'sev' : "251"}, {'fault' : "Alm", 'sev' : "501"}, {'fault' : "Warning", 'sev' : "251"}]
    pid_alarm_types = [{'fault' : "Alm", 'sev' : "501"}, {'fault' : "Warning", 'sev' : "251"}, {'fault' : "Man", 'sev' : "251"}, {'fault' : "Ignore", 'sev' : "251"}, {'fault' : "Fixed", 'sev' : "251"}, {'fault' : "LL", 'sev' : "501"}, {'fault' : "L", 'sev' : "251"}, {'fault' : "H", 'sev' : "251"}, {'fault' : "HH", 'sev' : "501"}]
    alm_alarm_types = [{'fault' : "Alm", 'sev' : "501"}, {'fault' : "Warning", 'sev' : "251"}, {'fault' : "Ignore", 'sev' : "251"}]
    vlv_alarm_types = [{'fault' : "Man", 'sev' : "251"}, {'fault' : "Ignore", 'sev' : "251"}, {'fault' : "FB_PAlm", 'sev' : "501"}, {'fault' : "FB_NAlm", 'sev' : "501"}]
    sum_alarm_types = [{'fault' : "Comm_Flt", 'sev' : "251"}, {'fault' : "Ignore", 'sev' : "251"}, {'fault' : "Voltage_H", 'sev' : "501"}, {'fault' : "Voltage_L", 'sev' : "501"}, {'fault' : "Voltage_LL", 'sev' : "501"}]

    frq_alarm_texts = ["Motor - Manual mode Warning", "Motor - Ignore active Warning", "Motor - Safety fault", "Drive - Amp Warning", "Drive - Torque Warning", "Drive - Thermal protection Alarm", "Motor - Disconnect turned off Alarm", "Drive - PTC thermal protection Alarm", "Drive - Run feedback Alarm", "Motor - Rotation feedback Alarm", "Drive - Drive fault Alarm",
				"Drive - Communication fault", "Drive - Any SW instuction within AOI has faultet", "Drive - Any Overload / Voltage fault", "Drive - PTC drive thermal protection Alarm", "Drive - Position error window exeeded", "Drive - Feedback fault including Encoder feedback", "Drive - Drive internal heat or overload fault", "Drive - Amp Alarm",
				"Drive - Torque Alarm", "Drive - Brake Resistor Too Hot"]
    mtr_alarm_texts = ["Manual mode Warning", "Ignore active Warning", "Thermal protection Alarm", "Disconnect turned off Alarm", "Safety fault", "Run feedback Alarm", "Rotation feedback Alarm", "Run reverse feedback Alarm", "Safety contactor feedback Fault"]
    ain_alarm_texts = ["Manual mode Warning", "Ignore active Warning", "Low-Low Alarm", "Low Warning", "High Warning", "High-High Alarm", "Overflow Alarm / Overload (>20 mA)", "Underflow Alarm / Wirebreak (< 4mA)"]
    aout_alarm_texts = ["Manual mode Warning", "Ignore active Warning", "Alarm", "Warning", "Feedback out of Range"]
    din_alarm_texts = ["Manual mode Warning", "Ignore active Warning", "Alarm", "Warning"]
    pid_alarm_texts = ["Alarm", "Warning", "Manual mode Warning", "Ignore active Warning", "Fixed Control Active", "Low Low Alarm", "Low Warning", "High Warning", "High High Alarm"]
    alm_alarm_texts = ["Alarm", "Warning", "Ignore"]
    vlv_alarm_texts = ["Manual mode Warning", "Ignore active Warning", "Valve positive Feedback Alarm", "Valve negative Feedback Alarm"]
    sum_alarm_texts = ["Communication Fault - Ethernet", "Ignore active Warning", "Voltage High Alarm", "Voltage Low Alarm", "Voltage Low Low Alarm"]

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
    etree.SubElement(PollGroups, 'PollGroupTags', rate="2").text = ""
    PollGroupTags = etree.SubElement(PollGroups, 'PollGroupTags', rate="5")

    # Create alarm tags
    for i in range(len(df)):
        identifier = df.loc[i, "Generator Function"]
        tag_name_raw = f'{df.loc[i, "TAG Part 2 (# Item)"]}'
        tag_name = tag_name_raw.replace(".1", "").replace(".2", "").replace(".3", "").replace(".4", "").replace(".5", "")
        if identifier == ("FRQ"):
            for o in frq_alarm_types:
                etree.SubElement(PollGroupTags, 'Tag').text = f'[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_{identifier}_UDT.E.{o["fault"]}'
        elif identifier == ("MTR"):
            for o in mtr_alarm_types:
                etree.SubElement(PollGroupTags, 'Tag').text = f'[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_{identifier}_UDT.E.{o["fault"]}'
        elif identifier == ("AIN"):
            for o in ain_alarm_types:
                etree.SubElement(PollGroupTags, 'Tag').text = f'[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_{identifier}_UDT.E.{o["fault"]}'
        elif identifier == ("AOUT"):
            for o in aout_alarm_types:
                etree.SubElement(PollGroupTags, 'Tag').text = f'[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_{identifier}_UDT.E.{o["fault"]}'
        elif identifier == ("DIN"):
            for o in din_alarm_types:
                etree.SubElement(PollGroupTags, 'Tag').text = f'[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_{identifier}_UDT.E.{o["fault"]}'
        elif identifier == ("PID"):
            for o in pid_alarm_types:
                etree.SubElement(PollGroupTags, 'Tag').text = f'[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_{identifier}_UDT.E.{o["fault"]}'
        elif identifier == ("ALM"):
            for o in alm_alarm_types:
                etree.SubElement(PollGroupTags, 'Tag').text = f'[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_{identifier}_UDT.E.{o["fault"]}'
        elif identifier == ("VLV"):
            for o in vlv_alarm_types:
                etree.SubElement(PollGroupTags, 'Tag').text = f'[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_{identifier}_UDT.E.{o["fault"]}'
        elif identifier == ("SUM"):
            for o in sum_alarm_types:
                etree.SubElement(PollGroupTags, 'Tag').text = f'[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_PM_UDT.E.{o["fault"]}'
    
    etree.SubElement(PollGroups, 'PollGroupTags', rate="10").text = ""
    etree.SubElement(PollGroups, 'PollGroupTags', rate="20").text = ""
    etree.SubElement(PollGroups, 'PollGroupTags', rate="30").text = ""
    etree.SubElement(PollGroups, 'PollGroupTags', rate="60").text = ""
    etree.SubElement(PollGroups, 'PollGroupTags', rate="120").text = ""

    FTAeDetectorCommand = etree.SubElement(Commands, 'FTAeDetectorCommand', style="FTAeDefaultDetector", version="11.0.0")
    etree.SubElement(FTAeDetectorCommand, 'Operation').text = "WriteMsg"
    Messages = etree.SubElement(FTAeDetectorCommand, 'Messages')

    # Create alarm messages
    msgid = int(AlmNr)
    area = str()
    for i in range(len(df)):
        identifier = df.loc[i, "Generator Function"]
        tag_name_mes = f'(+{df.loc[i, "TAG Part 2 (# Item)"]}={df.loc[i, "TAG Part 3 (Function code)"]}-{df.loc[i, "TAG Part 4 (# Function serial)"]})'
        if str(df.loc[i, "Sort"]) == "1" and pd.notna(df.loc[i, "Component Description"]): area = df.loc[i, "Component Description"]
        tag_part1 = f' - {df.loc[i, "TAG Part 1 (# System)"]}' if pd.notna(df.loc[i, "TAG Part 1 (# System)"]) else ""
        cmNr = df.loc[i, "CM No"]

        if identifier == ("FRQ"): # Create messages for FRQ
            tempdf = df.loc[df["CM No"] == cmNr]
            tempdf = tempdf.reset_index()
            tag_name_mes_frq_ptc = tag_name_mes
            tag_name_mes_frq_pro = tag_name_mes
            tag_name_mes_frq_r = tag_name_mes
            tag_name_mes_frq_dis = tag_name_mes
            tag_name_mes_frq_rot = tag_name_mes
            for x in range(len(tempdf)):
                if tempdf.loc[x, "Generator Function"] == "FRQ_Ptc":
                    tag_name_mes_frq_ptc = f'(+{tempdf.loc[x, "TAG Part 2 (# Item)"]}={tempdf.loc[x, "TAG Part 3 (Function code)"]}-{tempdf.loc[x, "TAG Part 4 (# Function serial)"]})'
                if tempdf.loc[x, "Generator Function"] == "FRQ_ETH":
                    ERLocation = tag_part1
                if tempdf.loc[x, "Generator Function"] == "FRQ_Pro":
                    tag_name_mes_frq_pro = f'(+{tempdf.loc[x, "TAG Part 2 (# Item)"]}={tempdf.loc[x, "TAG Part 3 (Function code)"]}-{tempdf.loc[x, "TAG Part 4 (# Function serial)"]})'
                    alm_desc_frq_pro = f'{tempdf.loc[x, "Process Description"]}'
                if tempdf.loc[x, "Generator Function"] == "FRQ_R":
                    tag_name_mes_frq_r = f'(+{tempdf.loc[x, "TAG Part 2 (# Item)"]}={tempdf.loc[x, "TAG Part 3 (Function code)"]}-{tempdf.loc[x, "TAG Part 4 (# Function serial)"]})'
                if tempdf.loc[x, "Generator Function"] == "FRQ_Dis":
                    tag_name_mes_frq_dis = f'(+{tempdf.loc[x, "TAG Part 2 (# Item)"]}={tempdf.loc[x, "TAG Part 3 (Function code)"]}-{tempdf.loc[x, "TAG Part 4 (# Function serial)"]})'
                if tempdf.loc[x, "Generator Function"] == "FRQ_Rot":
                    tag_name_mes_frq_rot = f'(+{tempdf.loc[x, "TAG Part 2 (# Item)"]}={tempdf.loc[x, "TAG Part 3 (Function code)"]}-{tempdf.loc[x, "TAG Part 4 (# Function serial)"]})'
            
            for o in frq_alarm_texts:
                msgid = msgid + 1
                Message = etree.SubElement(Messages, 'Message', id = str(msgid))
                Msgs = etree.SubElement(Message, 'Msgs')
                if "Drive - PTC" in o:
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {o} (Location {ERLocation}) {tag_name_mes_frq_ptc}\n'
                elif "Drive - Thermal" in o:
                    alm_desc_frq_pro = f' - {tempdf.loc[x, "Process Description"]}' if pd.notna(tempdf.loc[x, "Process Description"]) else ""
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {alm_desc_frq_pro} (Location {ERLocation}) {tag_name_mes_frq_pro}\n'
                elif "Drive - Brake" in o:
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {o} (Location {ERLocation}) {tag_name_mes_frq_r}\n'
                elif "Motor - Disconnect" in o:
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {o} {tag_name_mes_frq_dis}\n'
                elif "Motor - Rotation" in o:
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {o} {tag_name_mes_frq_rot}\n'
                elif "Drive" in o:
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {o} (Location {ERLocation}) {tag_name_mes}\n'
                elif "Motor" in o:
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {o} {tag_name_mes}\n'

        if identifier == ("MTR"): # Create messages for MTR
            tempdf = df.loc[df["CM No"] == cmNr]
            tempdf = tempdf.reset_index()
            tag_name_mes_mtr_dis = tag_name_mes
            tag_name_mes_mtr_pro = tag_name_mes
            tag_name_mes_mtr_rot = tag_name_mes
            tag_name_mes_mtr_run = tag_name_mes
            tag_name_mes_mtr_runRev = tag_name_mes
            tag_name_mes_mtr_safFb = tag_name_mes
            for x in range(len(tempdf)):
                if tempdf.loc[x, "Generator Function"] == "MTR_Dis":
                    tag_name_mes_mtr_dis = f'(+{tempdf.loc[x, "TAG Part 2 (# Item)"]}={tempdf.loc[x, "TAG Part 3 (Function code)"]}-{tempdf.loc[x, "TAG Part 4 (# Function serial)"]})'
                if tempdf.loc[x, "Generator Function"] == "MTR_Pro":
                    tag_name_mes_mtr_pro = f'(+{tempdf.loc[x, "TAG Part 2 (# Item)"]}={tempdf.loc[x, "TAG Part 3 (Function code)"]}-{tempdf.loc[x, "TAG Part 4 (# Function serial)"]})'
                    alm_desc_mtr_pro = f'{tempdf.loc[x, "Process Description"]}'
                if tempdf.loc[x, "Generator Function"] == "MTR_Rot":
                    tag_name_mes_mtr_rot = f'(+{tempdf.loc[x, "TAG Part 2 (# Item)"]}={tempdf.loc[x, "TAG Part 3 (Function code)"]}-{tempdf.loc[x, "TAG Part 4 (# Function serial)"]})'
                if tempdf.loc[x, "Generator Function"] == "MTR_Run":
                    tag_name_mes_mtr_run = f'(+{tempdf.loc[x, "TAG Part 2 (# Item)"]}={tempdf.loc[x, "TAG Part 3 (Function code)"]}-{tempdf.loc[x, "TAG Part 4 (# Function serial)"]})'
                    ERLocation = tag_part1     #tempdf.loc[x, "TAG Part 1 (# System)"]
                if tempdf.loc[x, "Generator Function"] == "MTR_Run_Rev":
                    tag_name_mes_mtr_runRev = f'(+{tempdf.loc[x, "TAG Part 2 (# Item)"]}={tempdf.loc[x, "TAG Part 3 (Function code)"]}-{tempdf.loc[x, "TAG Part 4 (# Function serial)"]})'
                if tempdf.loc[x, "Generator Function"] == "MTR_Saf_Fb":
                    tag_name_mes_mtr_safFb = f'(+{tempdf.loc[x, "TAG Part 2 (# Item)"]}={tempdf.loc[x, "TAG Part 3 (Function code)"]}-{tempdf.loc[x, "TAG Part 4 (# Function serial)"]})'

            for o in mtr_alarm_texts:
                msgid = msgid + 1
                Message = etree.SubElement(Messages, 'Message', id = str(msgid))
                Msgs = etree.SubElement(Message, 'Msgs')
                if "Disconnect turned off Alarm" in o:
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]} - {o} {tag_name_mes_mtr_dis}\n'
                elif "Thermal protection Alarm" in o:
                    alm_desc_mtr_pro = f' - {tempdf.loc[x, "Process Description"]}' if pd.notna(tempdf.loc[x, "Process Description"]) else ""
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]} - {alm_desc_mtr_pro} (Location {ERLocation}) {tag_name_mes_mtr_pro}\n'
                elif "Rotation feedback Alarm" in o:
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]} - {o} {tag_name_mes_mtr_rot}\n'
                elif "Run feedback Alarm" in o:
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]} - {o} (Location {ERLocation}) {tag_name_mes_mtr_run}\n'
                elif "Run reverse feedback Alarm" in o:
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]} - {o} (Location {ERLocation}) {tag_name_mes_mtr_runRev}\n'
                elif "Safety contactor feedback Fault" in o:
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]} - {o} (Location {ERLocation}) {tag_name_mes_mtr_safFb}\n'
                else:
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]} - {o} {tag_name_mes}\n'

        if identifier == ("AIN"):
            for o in ain_alarm_texts:
                msgid = msgid + 1
                Message = etree.SubElement(Messages, 'Message', id = str(msgid))
                Msgs = etree.SubElement(Message, 'Msgs')
                ERLocation = df.loc[i, "TAG Part 1 (# System)"]
                if pd.isna(df.loc[i, "TAG Part 1 (# System)"]):
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]} - {o} {tag_name_mes}\n'
                elif pd.notna(df.loc[i, "TAG Part 1 (# System)"]):
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]} - {o} (Location {ERLocation}) {tag_name_mes}\n'

        if identifier == ("AOUT"):
            for o in aout_alarm_texts:
                msgid = msgid + 1
                Message = etree.SubElement(Messages, 'Message', id = str(msgid))
                Msgs = etree.SubElement(Message, 'Msgs')
                ERLocation = df.loc[i, "TAG Part 1 (# System)"]
                if pd.isna(df.loc[i, "TAG Part 1 (# System)"]):
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]} - {o} {tag_name_mes}\n'
                elif pd.notna(df.loc[i, "TAG Part 1 (# System)"]):
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]} - {o} (Location {ERLocation}) {tag_name_mes}\n'

        if identifier == ("DIN"):
            for o in din_alarm_texts:
                msgid = msgid + 1
                Message = etree.SubElement(Messages, 'Message', id = str(msgid))
                Msgs = etree.SubElement(Message, 'Msgs')
                ERLocation = df.loc[i, "TAG Part 1 (# System)"]
                if pd.isna(df.loc[i, "TAG Part 1 (# System)"]):
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]} - {o} {tag_name_mes}\n'
                elif pd.notna(df.loc[i, "TAG Part 1 (# System)"]):
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]} - {o} (Location {ERLocation}) {tag_name_mes}\n'

        if identifier == ("PID"):
            for o in pid_alarm_texts:
                msgid = msgid + 1
                Message = etree.SubElement(Messages, 'Message', id = str(msgid))
                Msgs = etree.SubElement(Message, 'Msgs')
                ERLocation = df.loc[i, "TAG Part 1 (# System)"]
                if pd.isna(df.loc[i, "TAG Part 1 (# System)"]):
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]} - {o} {tag_name_mes}\n'
                elif pd.notna(df.loc[i, "TAG Part 1 (# System)"]):
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]} - {o} (Location {ERLocation}) {tag_name_mes}\n'

        if identifier == ("ALM"):
            for o in alm_alarm_texts:
                msgid = msgid + 1
                Message = etree.SubElement(Messages, 'Message', id = str(msgid))
                Msgs = etree.SubElement(Message, 'Msgs')
                ERLocation = df.loc[i, "TAG Part 1 (# System)"]
                if pd.isna(df.loc[i, "TAG Part 1 (# System)"]):
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]} - {o} {tag_name_mes}\n'
                elif pd.notna(df.loc[i, "TAG Part 1 (# System)"]):
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]} - {o} (Location {ERLocation}) {tag_name_mes}\n'

        if identifier == ("VLV"):
            tempdf = df.loc[df["CM No"] == cmNr]
            tempdf = tempdf.reset_index()
            tag_name_mes_vlv_p = tag_name_mes
            tag_name_mes_vlv_n = tag_name_mes
            for x in range(len(tempdf)):
                if tempdf.loc[x, "Generator Function"] == "VLV_P":
                    tag_name_mes_vlv_p = f'(+{tempdf.loc[x, "TAG Part 2 (# Item)"]}={tempdf.loc[x, "TAG Part 3 (Function code)"]}-{tempdf.loc[x, "TAG Part 4 (# Function serial)"]})'
                if tempdf.loc[x, "Generator Function"] == "VLV_N":
                    tag_name_mes_vlv_n = f'(+{tempdf.loc[x, "TAG Part 2 (# Item)"]}={tempdf.loc[x, "TAG Part 3 (Function code)"]}-{tempdf.loc[x, "TAG Part 4 (# Function serial)"]})'
            for o in vlv_alarm_texts:
                msgid = msgid + 1
                Message = etree.SubElement(Messages, 'Message', id = str(msgid))
                Msgs = etree.SubElement(Message, 'Msgs')
                if "Valve positive Feedback Alarm" in o:
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]} - {o} {tag_name_mes_vlv_p}\n'
                elif "Valve negative Feedback Alarm" in o:
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]} - {o} {tag_name_mes_vlv_n}\n'
                else:
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]} - {o} {tag_name_mes}\n'

        if identifier == ("SUM"):
            for o in sum_alarm_texts:
                msgid = msgid + 1
                Message = etree.SubElement(Messages, 'Message', id = str(msgid))
                Msgs = etree.SubElement(Message, 'Msgs')
                ERLocation = df.loc[i, "TAG Part 1 (# System)"]
                if pd.isna(df.loc[i, "TAG Part 1 (# System)"]):
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]} - {o} {tag_name_mes}\n'
                elif pd.notna(df.loc[i, "TAG Part 1 (# System)"]):
                    etree.SubElement(Msgs, 'Msg', {etree.QName(XMLNamespaces.xml, "lang"): "en-US"}).text = f'\n{area} - {df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]} - {o} (Location {ERLocation}) {tag_name_mes}\n'

    FTAeDetectorCommand = etree.SubElement(Commands, 'FTAeDetectorCommand', style="FTAeDefaultDetector", version="11.0.0")
    etree.SubElement(FTAeDetectorCommand, 'Operation').text = "WriteConfig"
    FTAlarmElements = etree.SubElement(FTAeDetectorCommand, 'FTAlarmElements', shelveMaxValue="480")

    msgid_tmp = int(AlmNr)
    for i in range(len(df)):
        identifier = df.loc[i, "Generator Function"]
        tag_name_mes = f'(+{df.loc[i, "TAG Part 2 (# Item)"]}={df.loc[i, "TAG Part 3 (Function code)"]}-{df.loc[i, "TAG Part 4 (# Function serial)"]})'
        tag_name_raw = f'{df.loc[i, "TAG Part 2 (# Item)"]}'
        tag_name = tag_name_raw.replace(".1", "").replace(".2", "").replace(".3", "").replace(".4", "").replace(".5", "")
        if str(df.loc[i, "Sort"]) == "1": area = df.loc[i, "Component Description"]
        if identifier == ("FRQ"):
            for o in frq_alarm_types:
                msgid_tmp = msgid_tmp + 1
                msgid = str(msgid_tmp).zfill(5) # Makes number always be 5 digits long
                FTAlarmElement = etree.SubElement(FTAlarmElements, 'FTAlarmElement', name=f'{msgid} Alarm', latched="false", ackRequired="true", style="Discrete")
                DiscreteElement = etree.SubElement(FTAlarmElement, 'DiscreteElement')
                etree.SubElement(DiscreteElement, 'DataItem').text = f'[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_{identifier}_UDT.E.{o["fault"]}'
                etree.SubElement(DiscreteElement, 'Style').text = "DiscreteTrue"
                etree.SubElement(DiscreteElement, 'Severity').text = o["sev"]
                etree.SubElement(DiscreteElement, 'DelayInterval').text = "0"
                etree.SubElement(DiscreteElement, 'EnableTag').text = "false"
                etree.SubElement(DiscreteElement, 'UserData')
                etree.SubElement(DiscreteElement, 'RSVCmd').text = f'\nDisplay $[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_{identifier}_UDT.S.DisplayName$; mUpdateMenubar\n'
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
                etree.SubElement(DiscreteElement, 'MessageID').text = str(msgid_tmp)
                etree.SubElement(DiscreteElement, 'Params').text = ""
        if identifier == ("MTR"):
            for o in mtr_alarm_types:
                msgid_tmp = msgid_tmp + 1
                msgid = str(msgid_tmp).zfill(5) # Makes number always be 5 digits long
                FTAlarmElement = etree.SubElement(FTAlarmElements, 'FTAlarmElement', name=f'{msgid} Alarm', latched="false", ackRequired="true", style="Discrete")
                DiscreteElement = etree.SubElement(FTAlarmElement, 'DiscreteElement')
                etree.SubElement(DiscreteElement, 'DataItem').text = f'[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_{identifier}_UDT.E.{o["fault"]}'
                etree.SubElement(DiscreteElement, 'Style').text = "DiscreteTrue"
                etree.SubElement(DiscreteElement, 'Severity').text = o["sev"]
                etree.SubElement(DiscreteElement, 'DelayInterval').text = "0"
                etree.SubElement(DiscreteElement, 'EnableTag').text = "false"
                etree.SubElement(DiscreteElement, 'UserData')
                etree.SubElement(DiscreteElement, 'RSVCmd').text = f'\nDisplay $[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_{identifier}_UDT.S.DisplayName$; mUpdateMenubar\n'
                etree.SubElement(DiscreteElement, 'AlarmClass')
                etree.SubElement(DiscreteElement, 'GroupID').text = "0"
                HandshakeTags = etree.SubElement(DiscreteElement, 'HandshakeTags')
                etree.SubElement(HandshakeTags, 'InAlarmDataItem')
                etree.SubElement(HandshakeTags, 'DisabledDataItem')
                etree.SubElement(HandshakeTags, 'AckedDataItem')
                etree.SubElement(HandshakeTags, 'SuppressedDataItem')
                etree.SubElement(HandshakeTags, 'ShelvedDataItem')
                etree.SubElement(DiscreteElement, 'RemoteAckAllDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteDisableDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteEnableDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteSuppressDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteUnSuppressDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteShelveAllDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteUnShelveDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteShelveDuration')
                etree.SubElement(DiscreteElement, 'MessageID').text = str(msgid_tmp)
                etree.SubElement(DiscreteElement, 'Params')
        if identifier == ("AIN"):
            for o in ain_alarm_types:
                msgid_tmp = msgid_tmp + 1
                msgid = str(msgid_tmp).zfill(5) # Makes number always be 5 digits long
                FTAlarmElement = etree.SubElement(FTAlarmElements, 'FTAlarmElement', name=f'{msgid} Alarm', latched="false", ackRequired="true", style="Discrete")
                DiscreteElement = etree.SubElement(FTAlarmElement, 'DiscreteElement')
                etree.SubElement(DiscreteElement, 'DataItem').text = f'[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_{identifier}_UDT.E.{o["fault"]}'
                etree.SubElement(DiscreteElement, 'Style').text = "DiscreteTrue"
                etree.SubElement(DiscreteElement, 'Severity').text = o["sev"]
                etree.SubElement(DiscreteElement, 'DelayInterval').text = "0"
                etree.SubElement(DiscreteElement, 'EnableTag').text = "false"
                etree.SubElement(DiscreteElement, 'UserData')
                etree.SubElement(DiscreteElement, 'RSVCmd').text = f'\nDisplay $[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_{identifier}_UDT.S.DisplayName$; mUpdateMenubar\n'
                etree.SubElement(DiscreteElement, 'AlarmClass')
                etree.SubElement(DiscreteElement, 'GroupID').text = "0"
                HandshakeTags = etree.SubElement(DiscreteElement, 'HandshakeTags')
                etree.SubElement(HandshakeTags, 'InAlarmDataItem')
                etree.SubElement(HandshakeTags, 'DisabledDataItem')
                etree.SubElement(HandshakeTags, 'AckedDataItem')
                etree.SubElement(HandshakeTags, 'SuppressedDataItem')
                etree.SubElement(HandshakeTags, 'ShelvedDataItem')
                etree.SubElement(DiscreteElement, 'RemoteAckAllDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteDisableDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteEnableDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteSuppressDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteUnSuppressDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteShelveAllDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteUnShelveDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteShelveDuration')
                etree.SubElement(DiscreteElement, 'MessageID').text = str(msgid_tmp)
                etree.SubElement(DiscreteElement, 'Params')
        if identifier == ("AOUT"):
            for o in aout_alarm_types:
                msgid_tmp = msgid_tmp + 1
                msgid = str(msgid_tmp).zfill(5) # Makes number always be 5 digits long
                FTAlarmElement = etree.SubElement(FTAlarmElements, 'FTAlarmElement', name=f'{msgid} Alarm', latched="false", ackRequired="true", style="Discrete")
                DiscreteElement = etree.SubElement(FTAlarmElement, 'DiscreteElement')
                etree.SubElement(DiscreteElement, 'DataItem').text = f'[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_{identifier}_UDT.E.{o["fault"]}'
                etree.SubElement(DiscreteElement, 'Style').text = "DiscreteTrue"
                etree.SubElement(DiscreteElement, 'Severity').text = o["sev"]
                etree.SubElement(DiscreteElement, 'DelayInterval').text = "0"
                etree.SubElement(DiscreteElement, 'EnableTag').text = "false"
                etree.SubElement(DiscreteElement, 'UserData')
                etree.SubElement(DiscreteElement, 'RSVCmd').text = f'\nDisplay $[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_{identifier}_UDT.S.DisplayName$; mUpdateMenubar\n'
                etree.SubElement(DiscreteElement, 'AlarmClass')
                etree.SubElement(DiscreteElement, 'GroupID').text = "0"
                HandshakeTags = etree.SubElement(DiscreteElement, 'HandshakeTags')
                etree.SubElement(HandshakeTags, 'InAlarmDataItem')
                etree.SubElement(HandshakeTags, 'DisabledDataItem')
                etree.SubElement(HandshakeTags, 'AckedDataItem')
                etree.SubElement(HandshakeTags, 'SuppressedDataItem')
                etree.SubElement(HandshakeTags, 'ShelvedDataItem')
                etree.SubElement(DiscreteElement, 'RemoteAckAllDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteDisableDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteEnableDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteSuppressDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteUnSuppressDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteShelveAllDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteUnShelveDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteShelveDuration')
                etree.SubElement(DiscreteElement, 'MessageID').text = str(msgid_tmp)
                etree.SubElement(DiscreteElement, 'Params')
        if identifier == ("DIN"):
            for o in din_alarm_types:
                msgid_tmp = msgid_tmp + 1
                msgid = str(msgid_tmp).zfill(5) # Makes number always be 5 digits long
                FTAlarmElement = etree.SubElement(FTAlarmElements, 'FTAlarmElement', name=f'{msgid} Alarm', latched="false", ackRequired="true", style="Discrete")
                DiscreteElement = etree.SubElement(FTAlarmElement, 'DiscreteElement')
                etree.SubElement(DiscreteElement, 'DataItem').text = f'[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_{identifier}_UDT.E.{o["fault"]}'
                etree.SubElement(DiscreteElement, 'Style').text = "DiscreteTrue"
                etree.SubElement(DiscreteElement, 'Severity').text = o["sev"]
                etree.SubElement(DiscreteElement, 'DelayInterval').text = "0"
                etree.SubElement(DiscreteElement, 'EnableTag').text = "false"
                etree.SubElement(DiscreteElement, 'UserData')
                etree.SubElement(DiscreteElement, 'RSVCmd').text = f'\nDisplay $[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_{identifier}_UDT.S.DisplayName$; mUpdateMenubar\n'
                etree.SubElement(DiscreteElement, 'AlarmClass')
                etree.SubElement(DiscreteElement, 'GroupID').text = "0"
                HandshakeTags = etree.SubElement(DiscreteElement, 'HandshakeTags')
                etree.SubElement(HandshakeTags, 'InAlarmDataItem')
                etree.SubElement(HandshakeTags, 'DisabledDataItem')
                etree.SubElement(HandshakeTags, 'AckedDataItem')
                etree.SubElement(HandshakeTags, 'SuppressedDataItem')
                etree.SubElement(HandshakeTags, 'ShelvedDataItem')
                etree.SubElement(DiscreteElement, 'RemoteAckAllDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteDisableDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteEnableDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteSuppressDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteUnSuppressDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteShelveAllDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteUnShelveDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteShelveDuration')
                etree.SubElement(DiscreteElement, 'MessageID').text = str(msgid_tmp)
                etree.SubElement(DiscreteElement, 'Params')
        if identifier == ("PID"):
            for o in pid_alarm_types:
                msgid_tmp = msgid_tmp + 1
                msgid = str(msgid_tmp).zfill(5) # Makes number always be 5 digits long
                FTAlarmElement = etree.SubElement(FTAlarmElements, 'FTAlarmElement', name=f'{msgid} Alarm', latched="false", ackRequired="true", style="Discrete")
                DiscreteElement = etree.SubElement(FTAlarmElement, 'DiscreteElement')
                etree.SubElement(DiscreteElement, 'DataItem').text = f'[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_{identifier}_UDT.E.{o["fault"]}'
                etree.SubElement(DiscreteElement, 'Style').text = "DiscreteTrue"
                etree.SubElement(DiscreteElement, 'Severity').text = o["sev"]
                etree.SubElement(DiscreteElement, 'DelayInterval').text = "0"
                etree.SubElement(DiscreteElement, 'EnableTag').text = "false"
                etree.SubElement(DiscreteElement, 'UserData')
                etree.SubElement(DiscreteElement, 'RSVCmd').text = f'\nDisplay $[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_{identifier}_UDT.S.DisplayName$; mUpdateMenubar\n'
                etree.SubElement(DiscreteElement, 'AlarmClass')
                etree.SubElement(DiscreteElement, 'GroupID').text = "0"
                HandshakeTags = etree.SubElement(DiscreteElement, 'HandshakeTags')
                etree.SubElement(HandshakeTags, 'InAlarmDataItem')
                etree.SubElement(HandshakeTags, 'DisabledDataItem')
                etree.SubElement(HandshakeTags, 'AckedDataItem')
                etree.SubElement(HandshakeTags, 'SuppressedDataItem')
                etree.SubElement(HandshakeTags, 'ShelvedDataItem')
                etree.SubElement(DiscreteElement, 'RemoteAckAllDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteDisableDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteEnableDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteSuppressDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteUnSuppressDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteShelveAllDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteUnShelveDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteShelveDuration')
                etree.SubElement(DiscreteElement, 'MessageID').text = str(msgid_tmp)
                etree.SubElement(DiscreteElement, 'Params')
        if identifier == ("ALM"):
            for o in alm_alarm_types:
                msgid_tmp = msgid_tmp + 1
                msgid = str(msgid_tmp).zfill(5) # Makes number always be 5 digits long
                FTAlarmElement = etree.SubElement(FTAlarmElements, 'FTAlarmElement', name=f'{msgid} Alarm', latched="false", ackRequired="true", style="Discrete")
                DiscreteElement = etree.SubElement(FTAlarmElement, 'DiscreteElement')
                etree.SubElement(DiscreteElement, 'DataItem').text = f'[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_{identifier}_UDT.E.{o["fault"]}'
                etree.SubElement(DiscreteElement, 'Style').text = "DiscreteTrue"
                etree.SubElement(DiscreteElement, 'Severity').text = o["sev"]
                etree.SubElement(DiscreteElement, 'DelayInterval').text = "0"
                etree.SubElement(DiscreteElement, 'EnableTag').text = "false"
                etree.SubElement(DiscreteElement, 'UserData')
                etree.SubElement(DiscreteElement, 'RSVCmd').text = f'\nDisplay $[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_{identifier}_UDT.S.DisplayName$; mUpdateMenubar\n'
                etree.SubElement(DiscreteElement, 'AlarmClass')
                etree.SubElement(DiscreteElement, 'GroupID').text = "0"
                HandshakeTags = etree.SubElement(DiscreteElement, 'HandshakeTags')
                etree.SubElement(HandshakeTags, 'InAlarmDataItem')
                etree.SubElement(HandshakeTags, 'DisabledDataItem')
                etree.SubElement(HandshakeTags, 'AckedDataItem')
                etree.SubElement(HandshakeTags, 'SuppressedDataItem')
                etree.SubElement(HandshakeTags, 'ShelvedDataItem')
                etree.SubElement(DiscreteElement, 'RemoteAckAllDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteDisableDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteEnableDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteSuppressDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteUnSuppressDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteShelveAllDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteUnShelveDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteShelveDuration')
                etree.SubElement(DiscreteElement, 'MessageID').text = str(msgid_tmp)
                etree.SubElement(DiscreteElement, 'Params')
        if identifier == ("VLV"):
            for o in vlv_alarm_types:
                msgid_tmp = msgid_tmp + 1
                msgid = str(msgid_tmp).zfill(5) # Makes number always be 5 digits long
                FTAlarmElement = etree.SubElement(FTAlarmElements, 'FTAlarmElement', name=f'{msgid} Alarm', latched="false", ackRequired="true", style="Discrete")
                DiscreteElement = etree.SubElement(FTAlarmElement, 'DiscreteElement')
                etree.SubElement(DiscreteElement, 'DataItem').text = f'[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_{identifier}_UDT.E.{o["fault"]}'
                etree.SubElement(DiscreteElement, 'Style').text = "DiscreteTrue"
                etree.SubElement(DiscreteElement, 'Severity').text = o["sev"]
                etree.SubElement(DiscreteElement, 'DelayInterval').text = "0"
                etree.SubElement(DiscreteElement, 'EnableTag').text = "false"
                etree.SubElement(DiscreteElement, 'UserData')
                etree.SubElement(DiscreteElement, 'RSVCmd').text = f'\nDisplay $[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_{identifier}_UDT.S.DisplayName$; mUpdateMenubar\n'
                etree.SubElement(DiscreteElement, 'AlarmClass')
                etree.SubElement(DiscreteElement, 'GroupID').text = "0"
                HandshakeTags = etree.SubElement(DiscreteElement, 'HandshakeTags')
                etree.SubElement(HandshakeTags, 'InAlarmDataItem')
                etree.SubElement(HandshakeTags, 'DisabledDataItem')
                etree.SubElement(HandshakeTags, 'AckedDataItem')
                etree.SubElement(HandshakeTags, 'SuppressedDataItem')
                etree.SubElement(HandshakeTags, 'ShelvedDataItem')
                etree.SubElement(DiscreteElement, 'RemoteAckAllDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteDisableDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteEnableDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteSuppressDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteUnSuppressDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteShelveAllDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteUnShelveDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteShelveDuration')
                etree.SubElement(DiscreteElement, 'MessageID').text = str(msgid_tmp)
                etree.SubElement(DiscreteElement, 'Params')
        if identifier == ("SUM"):
            for o in sum_alarm_types:
                msgid_tmp = msgid_tmp + 1
                msgid = str(msgid_tmp).zfill(5) # Makes number always be 5 digits long
                FTAlarmElement = etree.SubElement(FTAlarmElements, 'FTAlarmElement', name=f'{msgid} Alarm', latched="false", ackRequired="true", style="Discrete")
                DiscreteElement = etree.SubElement(FTAlarmElement, 'DiscreteElement')
                etree.SubElement(DiscreteElement, 'DataItem').text = f'[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_PM_UDT.E.{o["fault"]}'
                etree.SubElement(DiscreteElement, 'Style').text = "DiscreteTrue"
                etree.SubElement(DiscreteElement, 'Severity').text = o["sev"]
                etree.SubElement(DiscreteElement, 'DelayInterval').text = "0"
                etree.SubElement(DiscreteElement, 'EnableTag').text = "false"
                etree.SubElement(DiscreteElement, 'UserData')
                etree.SubElement(DiscreteElement, 'RSVCmd').text = f'\nDisplay $[plc{df.loc[i, "PLC No"]}]{tag_name}_{df.loc[i, "TAG Part 3 (Function code)"]}_{df.loc[i, "TAG Part 4 (# Function serial)"]}_PM_UDT.S.DisplayName$; mUpdateMenubar\n'
                etree.SubElement(DiscreteElement, 'AlarmClass')
                etree.SubElement(DiscreteElement, 'GroupID').text = "0"
                HandshakeTags = etree.SubElement(DiscreteElement, 'HandshakeTags')
                etree.SubElement(HandshakeTags, 'InAlarmDataItem')
                etree.SubElement(HandshakeTags, 'DisabledDataItem')
                etree.SubElement(HandshakeTags, 'AckedDataItem')
                etree.SubElement(HandshakeTags, 'SuppressedDataItem')
                etree.SubElement(HandshakeTags, 'ShelvedDataItem')
                etree.SubElement(DiscreteElement, 'RemoteAckAllDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteDisableDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteEnableDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteSuppressDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteUnSuppressDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteShelveAllDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteUnShelveDataItem', AutoReset="false")
                etree.SubElement(DiscreteElement, 'RemoteShelveDuration')
                etree.SubElement(DiscreteElement, 'MessageID').text = str(msgid_tmp)
                etree.SubElement(DiscreteElement, 'Params')

    tree = etree.ElementTree(FTAeAlarmStore)
    etree.indent(tree, space="")
    tree.write('export/rockwell/ftseAlarms/RA_FTSEAlarms_ALL.xml', pretty_print=True, encoding='utf-8', xml_declaration=True)

    with open('export/rockwell/ftseAlarms/RA_FTSEAlarms_ALL.xml', encoding="utf8") as f:
        tree = etree.parse(f)
        root = tree.getroot()

        for elem in root.getiterator():
            try:
                elem.text = elem.text.replace('&', 'and')
            except AttributeError:
                pass

    tree.write('export/rockwell/ftseAlarms/RA_FTSEAlarms_ALL.xml', pretty_print=True, encoding="utf-8", xml_declaration=True)