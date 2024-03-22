
from rest_framework.viewsets import ModelViewSet

from network_api.models import Router, Switch, NetworkSite
from network_api.serializers import RouterSerializer, SwitchSerializer, NetworkSiteSerializer


class SwitchViewSet(ModelViewSet):
    # permission_classes = [IsAdminUser]
    serializer_class = SwitchSerializer
    queryset = Switch.objects.all()


class RouterViewSet(ModelViewSet):
    # permission_classes = [IsAdminUser]
    serializer_class = RouterSerializer
    queryset = Router.objects.all()


class NetworkSiteViewSet(ModelViewSet):
    # permission_classes = [IsAdminUser]
    serializer_class = NetworkSiteSerializer
    queryset = NetworkSite.objects.all()
