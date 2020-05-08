from rest_framework.serializers import ModelSerializer

from . import models

class CampusSerializer(ModelSerializer):
    class Meta:
        model = models.Campus
        fields = "__all__"