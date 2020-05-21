from datetime import date, timedelta
from django.shortcuts import render
from django.db.models.deletion import ProtectedError
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import DestroyModelMixin
from rest_framework.response import Response
from rest_framework import status

from . import models, serializers

class CampusViewSet(ModelViewSet):
    queryset = models.Campus.objects.all()
    serializer_class = serializers.CampusSerializer
    def destroy(self, request, *args, **kwargs):
        try:
            return super(CampusViewSet, self).destroy(request, *args, **kwargs)
        except ProtectedError as e:
            return Response({"detail": [str(e)]}, status=status.HTTP_400_BAD_REQUEST)

class PersonViewSet(ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
    def destroy(self, request, *args, **kwargs):
        try:
            return super(PersonViewSet, self).destroy(request, *args, **kwargs)
        except ProtectedError as e:
            return Response({"detail": [str(e)]}, status=status.HTTP_400_BAD_REQUEST)

class TeacherViewSet(ModelViewSet):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer
    def destroy(self, request, *args, **kwargs):
        try:
            return super(TeacherViewSet, self).destroy(request, *args, **kwargs)
        except ProtectedError as e:
            return Response({"detail": [str(e)]}, status=status.HTTP_400_BAD_REQUEST)

class MajorViewSet(ModelViewSet):
    queryset = models.Major.objects.all()
    serializer_class = serializers.MajorSerializer
    def destroy(self, request, *args, **kwargs):
        try:
            return super(MajorViewSet, self).destroy(request, *args, **kwargs)
        except ProtectedError as e:
            return Response({"detail": [str(e)]}, status=status.HTTP_400_BAD_REQUEST)

class ClassViewSet(ModelViewSet):
    queryset = models.Class.objects.all()
    serializer_class = serializers.ClassSerializer
    def destroy(self, request, *args, **kwargs):
        try:
            return super(ClassViewSet, self).destroy(request, *args, **kwargs)
        except ProtectedError as e:
            return Response({"detail": [str(e)]}, status=status.HTTP_400_BAD_REQUEST)

class StudentViewSet(ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance.in_date + timedelta(days=4*365))
        if instance.in_date + timedelta(days=4*365) > date.today(): # 如果入学时间+4年>今天，那么不允许删除
            return Response({"detail": ["student haven't graduated"]}, status=status.HTTP_400_BAD_REQUEST)
        try:
            return super(StudentViewSet, self).destroy(request, *args, **kwargs)
        except ProtectedError as e:
            return Response({"detail": [str(e)]}, status=status.HTTP_400_BAD_REQUEST)

class CourseViewSet(ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    def destroy(self, request, *args, **kwargs):
        try:
            return super(CourseViewSet, self).destroy(request, *args, **kwargs)
        except ProtectedError as e:
            return Response({"detail": [str(e)]}, status=status.HTTP_400_BAD_REQUEST)

class CourseInfoViewSet(ModelViewSet):
    queryset = models.Course_Info.objects.all()
    serializer_class = serializers.CourseInfoSerializer
    def destroy(self, request, *args, **kwargs):
        try:
            return super(CourseInfoViewSet, self).destroy(request, *args, **kwargs)
        except ProtectedError as e:
            return Response({"detail": [str(e)]}, status=status.HTTP_400_BAD_REQUEST)

class CourseSelectionViewSet(ModelViewSet):
    queryset = models.Course_Selection.objects.all()
    serializer_class = serializers.CourseSelectionSerializer
    def destroy(self, request, *args, **kwargs):
        try:
            return super(CourseSelectionViewSet, self).destroy(request, *args, **kwargs)
        except ProtectedError as e:
            return Response({"detail": [str(e)]}, status=status.HTTP_400_BAD_REQUEST)

class StudentStatusChangeViewSet(ModelViewSet):
    queryset = models.Student_Status_Change.objects.all()
    serializer_class = serializers.StudentStatusChangeSerializer
    def destroy(self, request, *args, **kwargs):
        try:
            return super(StudentStatusChangeViewSet, self).destroy(request, *args, **kwargs)
        except ProtectedError as e:
            return Response({"detail": [str(e)]}, status=status.HTTP_400_BAD_REQUEST)
