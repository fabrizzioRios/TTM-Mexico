from rest_framework.response import Response
from rest_framework.views import APIView
from network_api.tools.netmiko_tools import DeviceTools


class DeviceConnectionView(APIView):
    def post(self, request):
        device_dictionary = DeviceTools.create_device_dictionary_from_request(request.data)
        if DeviceTools.device_connection(device_dictionary):
            data = {
                "device_connection": "Established",
                "connection": True,
            }
        else:
            data = {
                "device_connection": "Non-established",
                "connection": False
            }
        return Response(data)
