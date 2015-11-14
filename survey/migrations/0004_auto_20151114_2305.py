# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_autum_market'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autum',
            name='id',
        ),
        migrations.AlterField(
            model_name='autum',
            name='name',
            field=models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='客户姓名'),
        ),
    ]
