from rest_framework.response import Response
from rest_framework.views import APIView
from network_api.tools.other import Tool


class PingView(APIView):
    def post(self, request):
        if Tool.check_ping(request.data):
            return Response({'ping_status': 'completed', 'value': True})
        else:
            return Response({'unreachable': 'not_completed', 'value': False})
