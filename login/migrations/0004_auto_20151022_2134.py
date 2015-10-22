# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20151022_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='branch',
            field=models.CharField(max_length=4, choices=[('0071', '九沙支行'), ('0169', '月雅路支行'), ('0332', '朝阳支行'), ('0333', '营业中心'), ('0335', '德胜东路支行')], verbose_name='网点'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=11, null=True, verbose_name='手机号'),
        ),
    ]
