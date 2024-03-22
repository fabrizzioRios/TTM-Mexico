
from network_api.tools.netmiko_tools import DeviceTools

device_data_test = {
    'device_type': 'cisco_ios',
    'ip': '172.16.31.10',
    'username': 'pyclass',
    'password': 'test',
    'secret': 'test'
}

test = DeviceTools.device_connection(device_data_test)
print(test)
