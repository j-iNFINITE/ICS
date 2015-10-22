# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='branch',
            field=models.CharField(max_length=4, choices=[('0071', '九沙支行'), ('0169', '月雅路支行'), ('0332', '朝阳支行'), ('0333', '营业中心'), ('0335', '德胜东路支行')]),
        ),
    ]
