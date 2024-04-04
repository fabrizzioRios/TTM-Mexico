from netmiko_tools import DeviceTools
from other import Tool

def find_macadress(device_dict: dict, mac_address: str) -> dict:
    
    device_dictionary = DeviceTools.create_device_dictionary_from_request(device_dict)
    conection = DeviceTools.device_connection(device_dictionary)

    show_cdp_neighbors = DeviceTools.send_command_access_mode(conection, "show cdp neighbors")

    show_mac_add_table = DeviceTools.send_command_access_mode(conection, f"show mac address-table address {mac_address}")
    
    #GATHER THE CDP INTERFACE OUTPUT
    cdp_interface = Tool.filter_output('filter_plugin/cdpneighbors.textfsm', show_cdp_neighbors)
    
    cdp_list = [interface[1].replace(" ", "") for interface in cdp_interface]
    cdp_filtered = [elemento.replace('Gig', 'Gi') for elemento in cdp_list]

    #GATHER THE INTERFACE AND THE VLAN FROM THE MAC TABLE
    mac_parsed = Tool.filter_output('filter_plugin/macaddress.textfsm', show_mac_add_table)
    mac_list = [(mac_interface[3][0], mac_interface[2]) for mac_interface in mac_parsed]

    found = False

    if len(mac_list) != 0:

        for interfaz in mac_list:
            if interfaz[0] not in cdp_filtered:
                print(f"{interfaz[0]} is the interface for the mac address: {mac_address} in the vlan: {interfaz[1]}")
                found = True

                mac_response = {
                    "hostname": device_dict.get('hostname'),
                    "mac_address": mac_address,
                    "interface": interfaz[0],
                    "vlan": interfaz[1],
                    "found": found
                }

                break

            elif interfaz[0] in cdp_filtered:
                print(f"Found in {interfaz[0]} but it is not directly connected")

        if found == True: 

            return mac_response
        
        else:

            mac_response = {
                    "hostname": device_dict.get('hostname'),
                    "mac_address": mac_address,
                    "interface": "Not found",
                    "vlan": "NULL",
                    "found": found
                }
            
            return mac_response  

    else:
        print(f"{mac_address} was not found")
        
        mac_response = {
                    "hostname": device_dict.get('hostname'),
                    "mac_address": mac_address,
                    "interface": "Not found",
                    "vlan": "NULL",
                    "found": found
                }

        return mac_response
