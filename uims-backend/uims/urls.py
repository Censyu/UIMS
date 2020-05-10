from django.conf.urls import url,include
from rest_framework import routers
from . import views

routers = routers.DefaultRouter()
routers.register('campus', views.CampusViewSet)

urlpatterns = [
    url('', include(routers.urls)),
]