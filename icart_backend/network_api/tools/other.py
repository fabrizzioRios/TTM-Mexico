
import subprocess
import textfsm


class Tool:
    @classmethod
    def check_ping(cls,
                   ip_address: str) -> bool:
        try:
            result = subprocess.run(['ping', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if 'bytes=' in result.stdout or 'bytes=' in result.stderr:
                return True
            else:
                return False
        except Exception as err:
            return False
    
    @classmethod
    def filter_output(cls,
                      filter_path: str, stdout_output: str) -> list:

        with open(f'network_api/tools/{filter_path}.textfsm') as template_file:
            template = textfsm.TextFSM(template_file)
            result = template.ParseText(stdout_output)

        return result

    @classmethod
    def find_mac_address_in_list(cls,
                                 list_to_search: list, mac_address_to_search: str):
        try:
            element_found = next(item for item in list_to_search
                                 if item['mac_address'] == mac_address_to_search and
                                 item['value'])
            return element_found
        except Exception as err:
            return {
                "hostname": "Not found",
                "mac_address": mac_address_to_search,
                "interface": "Not found",
                "vlan": "None",
                "value": False
            }
