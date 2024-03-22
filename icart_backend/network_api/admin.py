from django.contrib import admin
from .models import Router, NetworkSite, Switch

admin.site.register(NetworkSite)
admin.site.register(Router)
admin.site.register(Switch)
