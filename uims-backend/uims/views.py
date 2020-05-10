from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from . import models, serializers

class CampusViewSet(ModelViewSet):
    queryset = models.Campus.objects.all()
    serializer_class = serializers.CampusSerializer
    
    # 主键不可修改，所以忽略主键，但是逻辑上这个好像不需要？
    # def perform_update(self, serializer):
    #     serializer.validated_data.pop('code', None)
    #     serializer.save()