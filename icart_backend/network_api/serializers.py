from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import PrimaryKeyRelatedField, HyperlinkedRelatedField, SlugRelatedField

from users.serializers import UserSerializer
from .models import Switch, Router, NetworkSite
from rest_framework.serializers import ModelSerializer


class NetworkSiteSerializer(ModelSerializer):
    administrator = UserSerializer(many=False, read_only=True)
    devices = SerializerMethodField(source='get_devices')

    class Meta:
        model = NetworkSite
        fields = '__all__'

    def get_devices(self, obj):
        switches_count = Switch.objects.filter(site=obj).count()
        routers_count = Router.objects.filter(site=obj).count()
        return routers_count + switches_count


class SwitchSerializer(ModelSerializer):
    site = serializers.PrimaryKeyRelatedField(queryset=NetworkSite.objects.all())

    class Meta:
        model = Switch
        fields = '__all__'


class RouterSerializer(ModelSerializer):
    site = serializers.PrimaryKeyRelatedField(queryset=NetworkSite.objects.all())

    class Meta:
        model = Router
        fields = '__all__'
