# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autum',
            name='name',
            field=models.CharField(verbose_name='客户姓名', max_length=12),
        ),
    ]
