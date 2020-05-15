from rest_framework.serializers import ModelSerializer

from . import models

class CampusSerializer(ModelSerializer):
    class Meta:
        model = models.Campus
        fields = "__all__"

class PersonSerializer(ModelSerializer):
    class Meta:
        model = models.Person
        fields = "__all__"

class TeacherSerializer(ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = "__all__"
    
    # 教师的身份证号在创建后不可变
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance is not None:
            self.fields.get('id').read_only = True

class MajorSerializer(ModelSerializer):
    class Meta:
        model = models.Major
        fields = "__all__"

class ClassSerializer(ModelSerializer):
    class Meta:
        model = models.Class
        fields = "__all__"

class StudentSerializer(ModelSerializer):
    class Meta:
        model = models.Student
        fields = "__all__"
    
    # 学生的身份证号在创建后不可变
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance is not None:
            self.fields.get('id').read_only = True

class CourseSerializer(ModelSerializer):
    class Meta:
        model = models.Course
        fields = "__all__"

class CourseInfoSerializer(ModelSerializer):
    class Meta:
        model = models.Course_Info
        fields = "__all__"

class CourseSelectionSerializer(ModelSerializer):
    class Meta:
        model = models.Course_Selection
        fields = "__all__"

class StudentStatusChangeSerializer(ModelSerializer):
    class Meta:
        model = models.Student_Status_Change
        fields = "__all__"
