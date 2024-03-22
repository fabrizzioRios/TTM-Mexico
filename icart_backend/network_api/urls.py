from django.urls import path, include
from .routers import router
from .views.PingView import PingView
from .views.DeviceConnectionView import DeviceConnectionView
from .views.DeviceSendCommandView import DeviceSendCommandView
from .views.MacAddressSearchView import MacAddressSearchView
from .views.GetDevicePerSiteView import GetDevicePerSiteView

urlpatterns = [
    path('', include(router.urls)),
    path('ping/', PingView.as_view(), name='device-ping'),
    path('ssh-connection/', DeviceConnectionView.as_view(), name='ssh-connection'),
    path('send-command/', DeviceSendCommandView.as_view(), name='send-command'),
    path('search-mac/', MacAddressSearchView.as_view(), name='search-mac'),
    path('devices-site/', GetDevicePerSiteView.as_view(), name='search-mac'),
]
