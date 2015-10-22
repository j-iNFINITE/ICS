from django.db import models
from django.contrib.auth.models import User
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    branchinfo = (
        ('0071','九沙支行'),
        ('0169','月雅路支行'),
        ('0332','朝阳支行'),
        ('0333','营业中心'),
        ('0335','德胜东路支行'),
    )
    branch = models.CharField('网点',max_length=4,choices=branchinfo)
    phone = models.IntegerField('手机号',max_length=11,null=True)
    level = (
        ('1','网点负责人'),
        ('2','客户经理'),
    )
    userlevel = models.CharField(max_length=1,choices=level)

