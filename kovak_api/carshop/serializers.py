from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers

from kovak_api.carshop.models import Car


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ["id", "nome", "modelo", "valor", "ano"]
