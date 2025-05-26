import clr

# working
#clr.AddReference("C:\\Users\\Saravanan\\OneDrive - Cedas India\\Study\\TIA-Tag tool\\TIA-Tag-tool\\PublicAPI\\V17\\Siemens.Engineering.dll")
#Export
clr.AddReference('C:\\Program Files\\Siemens\\Automation\\Portal V17\PublicAPI\\V17\\Siemens.Engineering.dll')


from System.IO import DirectoryInfo, FileInfo
import Siemens.Engineering as tia
import Siemens.Engineering.HW.Features as hwf
import Siemens.Engineering.HW;
import Siemens.Engineering.HW.Extensions;
import Siemens.Engineering.HW.Features;
import Siemens.Engineering.HW.Utilities;
import Siemens.Engineering.Compiler as comp
import Siemens.Engineering.Download as dl

import os
import pandas as pd

#df = pd.read_excel("C:/Users/ssace/Desktop/RA_Worksheet.xlsx", "HW")
#df.head()

def CreateHW(df, progress_callback):
    try:  
        # connect to an allready running instance (uncomment to use)

        processes = tia.TiaPortal.GetProcesses() # Making a list of all running processes
        #print (processes)

        process = processes[0]                   # Just taking the first process as an example
        Path = str(process.ProjectPath)
        #print (Path)
        mytia = process.Attach()
        myproject = mytia.Projects[0]
        #progress_callback.emit("Project : ", myproject)

        for i in range(len(df)):
            
            var1 = str(df.loc[i]["DeviceItemName"]) 
            var7 = str(df.loc[i]["DeviceName"]) 
            var2 = str(df.loc[i]["OrderNumber"]) 
            var3 = str(df.loc[i]["Version"])
            var4 = str(df.loc[i]["Type"])
            var5 = int(df.loc[i]["Slot"])
            var6 = str(df.loc[i]["Slot"]) #Comment IOx
            
            MLFB = "OrderNumber:"+var2+"/"+var3
            
            if(var4=="PLC" or var4 == "IM"or var4 == "Drive"):            
                print('Creating '+var4)
                #PLC1_mlfb = "OrderNumber:"+var2+"/"+var3
                D1 =  myproject.Devices.Find(var1)
                if D1 == None:
                    Device = myproject.Devices.CreateWithItem(MLFB, var1, var7)
                
            elif(var4=="IO"):
                print('Creating '+var4)
                #IOCards = "OrderNumber:"+var2+"/"+var3
                if (Device.DeviceItems[0].CanPlugNew(MLFB,var1,var5)):
                    Device.DeviceItems[0].PlugNew(MLFB,var1,var5)

        # Setting IP address and create a networking, compile all works well in python v3.7.13.
        # but it does not works here in python v3.9.2
        #Creating network, iosytem and setting IP adresses

        #creating a list of all found network interfaces on all stations in the station list
        print('Set IP address to the interfaces')
        n_interfaces = []
        n_devicename = []
        MemLastDeviceName = ''
        for device in myproject.Devices:
            print(device)
            device_item_aggregation = device.DeviceItems[1].DeviceItems
            for deviceitem in device_item_aggregation:
                print(deviceitem)
                network_service = tia.IEngineeringServiceProvider(deviceitem).GetService[hwf.NetworkInterface]()
                print(network_service)
                print(type(network_service))
                if type(network_service) is hwf.NetworkInterface:
                    device_name = device.GetAttribute("Name")                
                    var3 = df[df["DeviceName"] == device_name]["IP_Address"].values[0]
                    if (network_service.InterfaceType==3) and (MemLastDeviceName != device_name): # 3 - Profinet, 1- Profibus
                        MemLastDeviceName = device_name
                        n_interfaces.append(network_service)
                        n_devicename.append(device_name)
                        network_service.Nodes[0].SetAttribute('Address',var3)                                
                        print("Device Name : ", device_name)

        print("Interfaces : ", n_interfaces)
        print("Device Names : ", n_devicename)

        # Creating subnet and IO system on the first item in the list
        # Connects to subnet for remaining devices, if IO device it gets assigned to the IO system
        print('Create and connect to subnets')
        for n in n_interfaces:
            if n_interfaces.index(n) == 0:
                subnet = n_interfaces[0].Nodes[0].CreateAndConnectToSubnet("Profinet")
                ioSystem = n_interfaces[0].IoControllers[0].CreateIoSystem("PNIO")
            else:
                n_interfaces[n_interfaces.index(n)].Nodes[0].ConnectToSubnet(subnet)
                if (n_interfaces[n_interfaces.index(n)].IoConnectors.Count) >> 0:
                    n_interfaces[n_interfaces.index(n)].IoConnectors[0].ConnectToIoSystem(ioSystem)
    except Exception as e:            
                return ("error while create hardware configuration"+ str(e))