# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20151027_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_pd',
            name='hly',
            field=models.BooleanField(default=False, verbose_name='活利盈'),
        ),
        migrations.AddField(
            model_name='client_pd',
            name='lc',
            field=models.BooleanField(default=False, verbose_name='理财产品'),
        ),
        migrations.AddField(
            model_name='client_pd',
            name='shtk',
            field=models.BooleanField(default=False, verbose_name='商惠通卡'),
        ),
        migrations.AddField(
            model_name='client_pd',
            name='vip',
            field=models.BooleanField(default=False, verbose_name='vip'),
        ),
        migrations.AddField(
            model_name='client_pd',
            name='zjgj',
            field=models.BooleanField(default=False, verbose_name='资金归集'),
        ),
        migrations.AlterField(
            model_name='client_pd',
            name='zft',
            field=models.BooleanField(default=False, verbose_name='智付通'),
        ),
    ]
