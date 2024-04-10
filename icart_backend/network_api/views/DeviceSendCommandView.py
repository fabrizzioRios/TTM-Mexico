
from rest_framework.response import Response
from rest_framework.views import APIView
from network_api.tools.netmiko_tools import DeviceTools
import json


class DeviceSendCommandView(APIView):
    def post(self, request):
        device_data_str = request.data.get('device_data')
        command = request.data.get('writed_command')
        device_data = json.loads(device_data_str)
        connection_dictionary = DeviceTools.create_device_dictionary_from_request(device_data)
        if request.data.get('enable_mode') and not request.data.get('conf_mode'):
            result = DeviceTools.send_command_privilege_mode(connection_dictionary, command)
            print(result)
            return Response(result)
        elif not request.data.get('enable_mode') and request.data.get('conf_mode'):
            result = DeviceTools.send_command_config_mode(connection_dictionary, command)
            print(result)
            return Response(result)
        else:
            result = DeviceTools.send_command_access_mode(connection_dictionary, command)
            print(result)
            return Response(result)
