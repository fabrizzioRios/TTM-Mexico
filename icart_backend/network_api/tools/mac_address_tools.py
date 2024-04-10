
from network_api.tools.netmiko_tools import DeviceTools
from network_api.tools.other import Tool


def find_mac_adress(
        device_dict: dict, mac_address: str) -> dict:

    show_cdp_neighbors = DeviceTools.send_command_access_mode(device_dict, "show cdp neighbors")

    show_mac_add_table = DeviceTools.send_command_access_mode(device_dict,
                                                              f"show mac address-table address {mac_address}")

    # GATHER THE CDP INTERFACE OUTPUT
    cdp_interface = Tool.filter_output('cdpneighbors',
                                       show_cdp_neighbors.get('prompt_result'))

    cdp_list = [interface[1].replace(" ", "") for interface in cdp_interface]
    cdp_filtered = [elemento.replace('Gig', 'Gi') for elemento in cdp_list]

    # GATHER THE INTERFACE AND THE VLAN FROM THE MAC TABLE
    mac_parsed = Tool.filter_output('macaddress',
                                    show_mac_add_table.get('prompt_result'))
    mac_list = [(mac_interface[3][0], mac_interface[2]) for mac_interface in mac_parsed]

    if mac_list:
        for interfaz in mac_list:
            if interfaz[0] not in cdp_filtered:
                return {
                    "hostname": device_dict.get('host'),
                    "mac_address": mac_address,
                    "interface": interfaz[0],
                    "vlan": interfaz[1],
                    "value": True
                }
    else:
        return {
            "hostname": device_dict.get('host'),
            "mac_address": mac_address,
            "interface": "Not found",
            "vlan": "None",
            "value": False
        }
