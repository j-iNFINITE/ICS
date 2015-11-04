from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class market(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return str(self.name)

class client_info(models.Model):
    client_ID = models.CharField(max_length=16,primary_key=True) # ID
    client_NAME = models.TextField()  # 客户姓名
    client_GENDER = models.CharField(max_length=1,choices=(('M','男性'),('F','女性'),))  # 性别
    client_PHONE = models.CharField(max_length=11)  # 客户手机号
    client_ADDRESS = models.TextField()
    client_MARKET = models.ForeignKey(market)  # 所属市场
    client_MANAGER = models.ForeignKey(User)  # 管户经理
    def __str__(self):
        return str(self.client_ID)

class client_balance(models.Model):
    client_ID = models.ForeignKey(client_info)  #ID
    balance_date = models.CharField(max_length=8)  # 日期
    month_deposit = models.DecimalField('杭州月均',max_digits=11,decimal_places=2)  # 杭州月均
    month_fa = models.DecimalField('杭州月均金融',max_digits=11,decimal_places=2)  # 杭州月均金融
    jbmonth_deposit = models.DecimalField('九堡月均',max_digits=11,decimal_places=2)  # 九堡月均
    jbmonth_fa = models.DecimalField('九堡月均金融',max_digits=11,decimal_places=2)  # 九堡月均金融
    def __str__(self):
        return str(self.client_ID)

class client_pd(models.Model):
    client_ID=models.ForeignKey(client_info)
    zft = models.BooleanField('智付通',default=False)
    hly = models.BooleanField('活利盈',default=False)
    vip = models.BooleanField('vip',default=False)
    shtk = models.BooleanField('商惠通卡',default=False)
    lc = models.BooleanField('理财产品',default=False)
    zjgj = models.BooleanField('资金归集',default=False)
    def __str__(self):
        return str(self.client_ID)
# class answer(models.Model):


