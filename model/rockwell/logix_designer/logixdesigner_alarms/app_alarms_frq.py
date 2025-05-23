from lxml import etree
import pandas as pd

# ---Create alarms for frequency inverters---

def getFRQ(df):
    xml_doc = etree.Element('AlarmCollection')

    alarm_types = [{'fault' : "Alarm", 'sev' : "501"}, 
                   {'fault' : "Warning", 'sev' : "251"},
                   {'fault' : "Manual Mode Warning", 'sev' : "251"},
                   {'fault' : "Ignore Active Warning", 'sev' : "251"},
                   {'fault' : "Safety Fault", 'sev' : "501"},
                   {'fault' : "Amp Warning", 'sev' : "251"},
                   {'fault' : "Torque Warning", 'sev' : "251"},
                   {'fault' : "Amp Alarm", 'sev' : "501"},
                   {'fault' : "Torque Alarm", 'sev' : "501"},
                   {'fault' : "Thermal Protection", 'sev' : "501"},
                   {'fault' : "Disconnect Turned Off Alarm", 'sev' : "501"},
                   {'fault' : "PTC Thermal Protection Alarm", 'sev' : "501"},
                   {'fault' : "Run Feedback Alarm", 'sev' : "501"},
                   {'fault' : "Rotation Feedback Alarm", 'sev' : "501"},
                   {'fault' : "Drive Fault Alarm", 'sev' : "501"},
                   {'fault' : "Communication Fault", 'sev' : "501"},
                   {'fault' : "Any SW Instruction Within AOI Has Faulted", 'sev' : "501"},
                   {'fault' : "Any Overload/Voltage Fault", 'sev' : "501"},
                   {'fault' : "PTC Drive Thermal Protection Alarm", 'sev' : "501"},
                   {'fault' : "Position Error Window Exceeded", 'sev' : "501"},
                   {'fault' : "Feedback Fault, Including Encoder Feedback", 'sev' : "501"},
                   {'fault' : "Drive Internal Heat or Overload fault", 'sev' : "501"},
                   {'fault' : "Drive - Brake Resistor Too Hot", 'sev' : "501"}
                   ]

    for i in range(len(df)):
        identifier = df.loc[i, "Generator Function"]
        if identifier == ("FRQ"):
            Dint_nr = -1
            for o in alarm_types:
                Dint_nr = Dint_nr + 1
                tag_alarmclass = ''
                tag_hmigroup = ''
                tag_hmicmd = ''
                tag_name_mes = "+"+df.loc[i, "TAG Part 2 (# Item)"]+"="+df.loc[i, "TAG Part 3 (Function code)"]+"-"+df.loc[i, "TAG Part 4 (# Function serial)"]
                tagPart2 = df.loc[i, "TAG Part 2 (# Item)"]
                tagPart2_noDot = tagPart2.split('.', 1)[0]
                no_dot_name = tagPart2_noDot+"_"+df.loc[i, "TAG Part 3 (Function code)"]+"_"+df.loc[i, "TAG Part 4 (# Function serial)"]
                Alarm = etree.SubElement(xml_doc, 'Alarm', Name=f'FRQ_{no_dot_name}_ALM_DINT_{Dint_nr}', ConditionType="TRIP", Input=f'{no_dot_name}_ALM_DINT.{Dint_nr}', Expression="= 1", Limit="0", TargetTag="", OnDelay="0", OffDelay="0", Deadband="0", Severity=o['sev'], AssocTag1="", AssocTag2="", AssocTag3="", AssocTag4="", ShelveDuration="0", MaxShelveDuration="0", EvaluationPeriod="500", Latched="False", AckRequired="False", AlarmSetRollupIncluded="True", AlarmSetOperIncluded="True", Lang="en-US", Use="True", AlarmDefinition="")
                etree.SubElement(Alarm, 'Message',).text = f'{df.loc[i, "Component Description"]} - {df.loc[i, "Process Description"]} - {o["fault"]} ({tag_name_mes})'
                etree.SubElement(Alarm, 'AlarmClass').text = tag_alarmclass
                etree.SubElement(Alarm, 'HMIGroup').text = tag_hmigroup
                etree.SubElement(Alarm, 'HMICmd').text = tag_hmicmd

    tree = etree.ElementTree(xml_doc)
    tree.write('export/rockwell/alarms/RA_Alarms_FRQ.xml', pretty_print=True, encoding="utf-8", xml_declaration=True)

