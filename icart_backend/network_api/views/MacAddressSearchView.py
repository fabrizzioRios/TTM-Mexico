from rest_framework.response import Response
from rest_framework.views import APIView
from network_api.models import Switch
from network_api.tools.netmiko_tools import DeviceTools
from network_api.tools.mac_address_tools import find_mac_adress
from network_api.tools.other import Tool


class MacAddressSearchView(APIView):
    def post(self, request):
        mac_address = request.data.get('mac_address')
        switches = Switch.objects.all()
        dictionary_list = [DeviceTools.create_device_dictionary_from_queryset(element) for element in switches]
        print(dictionary_list)
        mac_address_shows = [find_mac_adress(element, mac_address) for element in dictionary_list]
        mac_address_result = Tool.find_mac_address_in_list(mac_address_shows, mac_address)
        print(mac_address_result)
        return Response(mac_address_result)
