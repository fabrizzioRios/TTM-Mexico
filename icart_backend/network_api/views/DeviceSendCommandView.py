from rest_framework.response import Response
from rest_framework.views import APIView
from network_api.tools.netmiko_tools import DeviceTools
import json


class DeviceSendCommandView(APIView):
    def post(self, request):
        print(request.data)
        device_data_str = request.data.get('device_data')
        print(device_data_str)
        command = request.data.get('writed_command')
        device_data = json.loads(device_data_str)
        connection_dictionary = DeviceTools.create_device_dictionary_from_request(device_data)
        ssh_device_connection = DeviceTools.device_connection(connection_dictionary)

        if request.data.get('enable_mode'):
            return Response(DeviceTools.send_command_privilege_mode(ssh_device_connection, command))
        if request.data.get('conf_mode'):
            return Response(DeviceTools.send_command_config_mode(ssh_device_connection, command))
        if request.data.get('from_file'):
            config_file = request.FILES['file'].read().decode('utf-8')
            print(config_file)
            return Response(DeviceTools.send_command_from_file(ssh_device_connection, config_file))
        else:
            return Response(DeviceTools.send_command_access_mode(ssh_device_connection, command))
