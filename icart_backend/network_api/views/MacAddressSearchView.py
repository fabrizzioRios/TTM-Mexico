from rest_framework.response import Response
from rest_framework.views import APIView
from network_api.models import Switch
from network_api.tools.netmiko_tools import DeviceTools


class MacAddressSearchView(APIView):
    def post(self, request):
        mac_address = request.data.get('mac_address')
        switches = Switch.objects.all()
        dictionary_list = [DeviceTools.create_device_dictionary_from_queryset(element) for element in switches]
        ssh_device_list = [DeviceTools.device_connection(element) for element in dictionary_list]
        mac_address_shows = [DeviceTools.search_mac(element, "sh mac address-table") for element in ssh_device_list]

        print(dictionary_list)

        print(ssh_device_list)
        return Response(mac_address)
