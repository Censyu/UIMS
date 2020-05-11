from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from . import models, serializers

class CampusViewSet(ModelViewSet):
    queryset = models.Campus.objects.all()
    serializer_class = serializers.CampusSerializer

class PersonViewSet(ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer

class TeacherViewSet(ModelViewSet):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer

class MajorViewSet(ModelViewSet):
    queryset = models.Major.objects.all()
    serializer_class = serializers.MajorSerializer

class ClassViewSet(ModelViewSet):
    queryset = models.Class.objects.all()
    serializer_class = serializers.ClassSerializer

class StudentViewSet(ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

class CourseViewSet(ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

class CourseInfoViewSet(ModelViewSet):
    queryset = models.Course_Info.objects.all()
    serializer_class = serializers.CourseInfoSerializer

class CourseSelectionViewSet(ModelViewSet):
    queryset = models.Course_Selection.objects.all()
    serializer_class = serializers.CourseSelectionSerializer

class StudentStatusChangeViewSet(ModelViewSet):
    queryset = models.Student_Status_Change.objects.all()
    serializer_class = serializers.StudentStatusChangeSerializer
