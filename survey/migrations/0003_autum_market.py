# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20151113_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='autum',
            name='market',
            field=models.CharField(max_length=30, default='', verbose_name='所属市场'),
            preserve_default=False,
        ),
    ]
