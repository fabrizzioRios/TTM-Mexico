from rest_framework.response import Response
from rest_framework.views import APIView
from network_api.tools.netmiko_tools import DeviceTools
import json


class DeviceSendCommandFileView(APIView):
    def post(self, request):
        device_data_str = request.data.get('device_data')
        device_data = json.loads(device_data_str)
        connection_dictionary = DeviceTools.create_device_dictionary_from_request(device_data)
        config_file = request.FILES['file'].read().decode('utf-8')
        result = DeviceTools.send_command_config_mode(connection_dictionary, config_file)
        print(result)
        return Response(result)
