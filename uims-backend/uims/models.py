from django.db import models

class Campus(models.Model):
    # 这里的最大长度是我随意设置的，请根据具体的数据库模型再修改！
    code = models.CharField(primary_key=True, max_length=10, help_text="校区代码")
    name = models.CharField(max_length=50, help_text="校区名称")
    address = models.CharField(max_length=50, help_text="校区地址")

# TODO 其他的数据库模型