from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
class Campus(models.Model):
    code = models.CharField(primary_key=True, max_length=10, help_text="校区代码")
    name = models.CharField(max_length=20, help_text="校区名称")
    address = models.CharField(max_length=30, help_text="校区地址")

    def __str__(self):
        return "campus : %s " % self.name

class Person(models.Model):
    id_type_choices = models.TextChoices('id_type','ID_Card, Passport') 
    gender_type = models.TextChoices('gender', (('M','Male'), ('F','Female'))) 

    id = models.CharField(primary_key=True, max_length=20, help_text="身份证号")
    chinese_name =  models.CharField(max_length=20, help_text="中文名")
    birth_date = models.DateField(help_text = "出生日期")
    id_type = models.CharField(choices=id_type_choices.choices, max_length=10, help_text="身份证件类型")
    gender = models.CharField(choices=gender_type.choices, max_length=6, help_text="性别")
    country = models.CharField(max_length=20, help_text="国籍")
    email =  models.CharField(max_length=50, help_text="电子邮箱")
    home_address =  models.CharField(blank = True,null=True,max_length=20, help_text="家庭住址")
    home_zipcode =  models.CharField(blank = True,null=True, max_length=10, help_text="家庭邮政编码")
    home_phone_num =  models.CharField(blank = True,null=True, max_length=10, help_text="家庭电话")

    def __str__(self):
        return "person : %s " % self.chinese_name

class Teacher(models.Model):
    title_type = models.TextChoices('title_type','Assistant_Professor Professor')

    work_id = models.CharField(primary_key=True, max_length=10, help_text="工号")
    in_date = models.DateField(help_text = "入职年月")
    id = models.OneToOneField(Person, on_delete=models.PROTECT, help_text="身份证件号")
    title = models.CharField(choices=title_type.choices, max_length=20, help_text="职称")
    major_code = models.ForeignKey('Major',  blank=True, null=True, on_delete=models.PROTECT, help_text="专业代码")

    def __str__(self):
        return "teacher : %s " % self.work_id

class Major(models.Model):
    code = models.CharField(primary_key=True, max_length=10, help_text="专业代码")
    name = models.CharField(max_length=20, help_text="专业名称")
    address = models.CharField(max_length=30, help_text="专业地址")
    campus_code = models.ForeignKey(Campus, on_delete=models.PROTECT, help_text="所属校区代码")
    director_id = models.OneToOneField(Teacher, blank=True, null=True, on_delete=models.PROTECT, help_text="专业负责人工号")

    def __str__(self):
        return "major : %s " % self.name

class Class(models.Model):
    code = models.CharField(primary_key=True, max_length=10, help_text="班级代码")
    name = models.CharField(max_length=20, help_text="班级名称")
    start_date = models.DateField(help_text = "建班年月")
    grade = models.IntegerField(help_text = "年级",
                                validators=[MaxValueValidator(3000),MinValueValidator(1800)])
    major_code = models.ForeignKey(Major, on_delete=models.PROTECT,  help_text="所属专业")
    mentor_work_id = models.OneToOneField(Teacher, on_delete=models.PROTECT,  help_text="班主任工号")

    def __str__(self):
        return "class : %s " % self.name


class Student(models.Model):
    student_id = models.CharField(primary_key=True, max_length=10, help_text="学号")
    in_date = models.DateField(help_text = "入学年月")
    id = models.OneToOneField(Person, on_delete=models.PROTECT, help_text="身份证件号")
    class_code = models.ForeignKey(Class, on_delete=models.PROTECT,  help_text="所属班级代码")
    
    def __str__(self):
        return "student : %s " % self.student_id

class Course(models.Model):
    evaluation_method_type = models.TextChoices('evaluation method type','Exam In-class_Presentation')

    id  = models.CharField(primary_key=True, max_length=10, help_text="课程编号")
    name = models.CharField(max_length=20, help_text="课程名称")
    evaluation_method = models.CharField(choices=evaluation_method_type.choices, max_length=25, help_text="考核方式")
    major_code = models.ForeignKey(Major, on_delete=models.PROTECT,  help_text="开课专业")
    
    def __str__(self):
        return "course : %s " % self.name

class Course_Info(models.Model):
    semester_type = models.TextChoices('semester_type', 'Spring Autumn')

    id  = models.CharField(primary_key=True, max_length=10, help_text="开课信息编号")
    year = models.DateField(help_text = "开课日期（年）")
    semester = models.CharField(choices=semester_type.choices, max_length=20, help_text="开课学期")
    time = models.CharField(max_length=20, help_text="开课时间")
    teacher_work_id = models.ForeignKey(Teacher, on_delete=models.PROTECT,help_text="开课教师工号")
    course_id = models.ForeignKey(Course, on_delete=models.PROTECT,help_text="课程编号")
    
    def __str__(self):
        return "course infomation : %s " % self.id

class Course_Selection(models.Model):

    student_id = models.ForeignKey(Student, on_delete=models.PROTECT, help_text="选课学生学号")
    course_info_id = models.ForeignKey(Course_Info, on_delete=models.PROTECT, help_text="开课信息编号")
    score = models.IntegerField(blank=True, null=True, help_text = "成绩")

    class Meta:
        unique_together = ['student_id', 'course_info_id']
    def __str__(self):
        return "course selection : %s " % self.student_id

class Student_Status_Change(models.Model):
    downgrade_reason_type = models.TextChoices('downgrade_reason_type', 'Suspend Volunter_Aid_Education')
    membership_transfer_type = (('Y', 'Yes'),('N', 'No'),('NM', 'Not A Member') )

    id =  models.CharField(primary_key=True, max_length=10, help_text="学籍异动编号")
    date =  models.DateField(help_text = "学籍异动日期")
    student_id = models.OneToOneField(Student, on_delete=models.PROTECT, help_text="学生学号")
    origin_class_code = models.ForeignKey(Class, related_name = "origin_class_code", on_delete=models.PROTECT, help_text="原班级编号")
    new_class_code = models.ForeignKey(Class, related_name = "new_class_code", on_delete=models.PROTECT, help_text="现班级编号")
    downgrade_reason = models.CharField(blank = True, null=True, choices=downgrade_reason_type.choices, max_length=25,help_text="降级原因")
    membership_transfer = models.CharField(blank = True, null=True, choices=membership_transfer_type,max_length=10, help_text="是否转出团员关系")

    def __str__(self):
        return "student status change : %s " % self.id
