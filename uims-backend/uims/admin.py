from django.contrib import admin
from . import models

admin.site.register(models.Campus)
admin.site.register(models.Person)
admin.site.register(models.Teacher)
admin.site.register(models.Major)
admin.site.register(models.Class)
admin.site.register(models.Student)
admin.site.register(models.Course)
admin.site.register(models.Course_Info)
admin.site.register(models.Course_Selection)
admin.site.register(models.Student_Status_Change)