from django.db import models
from users.models import User


class NetworkSite(models.Model):
    site_name = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    administrator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class Switch(models.Model):
    hostname = models.CharField(max_length=50, blank=True, null=True)
    admin_vlan = models.IntegerField(default=0)
    ip_address = models.CharField(max_length=16, blank=True, null=True)
    device_type = models.CharField(max_length=20, blank=True, null=True)
    domain_ssh = models.CharField(max_length=225, blank=True, null=True)
    username = models.CharField(max_length=15, blank=True, null=True)
    vtp_role = models.CharField(max_length=12, blank=True, null=True)
    vtp_domain_name = models.CharField(max_length=15, blank=True, null=True)
    site = models.ForeignKey(NetworkSite, on_delete=models.CASCADE, blank=True, null=True)


class Router(models.Model):
    hostname = models.CharField(max_length=50, blank=True, null=True)
    ip_address = models.CharField(max_length=16, blank=True, null=True)
    device_type = models.CharField(max_length=20, blank=True, null=True)
    domain_ssh = models.CharField(max_length=225, blank=True, null=True)
    username = models.CharField(max_length=15, blank=True, null=True)
    site = models.ForeignKey(NetworkSite, on_delete=models.CASCADE, blank=True, null=True)
