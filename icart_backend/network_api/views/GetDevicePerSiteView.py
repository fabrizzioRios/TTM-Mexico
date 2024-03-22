from rest_framework.response import Response
from rest_framework.views import APIView
from network_api.models import Switch, Router
from network_api.serializers import SwitchSerializer, RouterSerializer


class GetDevicePerSiteView(APIView):
    def post(self, request):
        devices_switches = Switch.objects.all()
        devices_routers = Router.objects.all()

        data = SwitchSerializer(devices_switches, many=True).data + RouterSerializer(devices_routers, many=True).data
        print(data)
        if data:
            return Response(data)
