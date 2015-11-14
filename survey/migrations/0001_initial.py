# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='autum',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='客户姓名')),
                ('hly', models.BooleanField(verbose_name='活利盈', default=False)),
                ('skb', models.BooleanField(verbose_name='收款宝', default=False)),
                ('sxt', models.BooleanField(verbose_name='随薪通准贷记卡', default=False)),
                ('kkt', models.BooleanField(verbose_name='卡卡通', default=False)),
                ('branch', models.CharField(verbose_name='网点', choices=[('0071', '九沙支行'), ('0169', '月雅路支行'), ('0332', '朝阳支行'), ('0333', '营业中心'), ('0335', '德胜东路支行')], max_length=4)),
                ('worker', models.CharField(verbose_name='受理员工', max_length=10)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
