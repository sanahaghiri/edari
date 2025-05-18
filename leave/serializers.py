from rest_framework import serializers
from .models import *


class LeaveSerializers(serializers.ModelSerializer):
    class Meta:
        model = LeaveModel
        fields = "__all__"
class LeaveGetSerializers(serializers.ModelSerializer):
    class Meta:
        model = LeaveModel
        fields = "__all__"
        depth = 1