from django.conf.urls import url,include
from rest_framework import routers
from . import views

routers = routers.DefaultRouter()
routers.register('campus', views.CampusViewSet)
routers.register('person', views.PersonViewSet)
routers.register('teacher', views.TeacherViewSet)
routers.register('major', views.MajorViewSet)
routers.register('class', views.ClassViewSet)
routers.register('student', views.StudentViewSet)
routers.register('course', views.CourseViewSet)
routers.register('course-info', views.CourseInfoViewSet)
routers.register('course-selection', views.CourseSelectionViewSet)
routers.register('student-status-change', views.StudentStatusChangeViewSet)

urlpatterns = [
    url('', include(routers.urls)),
]