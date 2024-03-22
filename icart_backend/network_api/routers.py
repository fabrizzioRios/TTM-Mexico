
from rest_framework.routers import DefaultRouter
from network_api.viewsets.viewsets import SwitchViewSet, RouterViewSet, NetworkSiteViewSet


router = DefaultRouter()

router.register(
    "routers",
    RouterViewSet,
    basename="router-viewsets"
)
router.register(
    "switches",
    SwitchViewSet,
    basename="switches-viewsets"
)
router.register(
    "network_site",
    NetworkSiteViewSet,
    basename="network-site-viewsets"
)
