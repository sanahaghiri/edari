from rest_framework import serializers
from .models import *


class PersonelSerializers(serializers.ModelSerializer):
    class Meta:
        model = PersonelModel
        fields = "__all__"


class LoginSerializer(serializers.Serializer):
    person_code = serializers.CharField()
    password = serializers.CharField()

