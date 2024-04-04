from rest_framework.response import Response
from rest_framework.views import APIView
from network_api.models import Switch
from network_api.tools.netmiko_tools import DeviceTools
from network_api.tools.mac_address_tools import find_macadress


class MacAddressSearchView(APIView):
    def post(self, request):
        mac_address = request.data.get('mac_address')
        switches = Switch.objects.all()
        dictionary_list = [DeviceTools.create_device_dictionary_from_queryset(element) for element in switches]
        mac_address_shows = [find_macadress(element, mac_address) for element in dictionary_list]

        print(mac_address_shows)

        return Response(mac_address)
