# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import client.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client_balance',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('balance_date', models.CharField(max_length=8)),
                ('month_deposit', models.DecimalField(max_digits=11, verbose_name='杭州月均', decimal_places=2)),
                ('month_fa', models.DecimalField(max_digits=11, verbose_name='杭州月均金融', decimal_places=2)),
                ('jbmonth_deposit', models.DecimalField(max_digits=11, verbose_name='九堡月均', decimal_places=2)),
                ('jbmonth_fa', models.DecimalField(max_digits=11, verbose_name='九堡月均金融', decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='client_info',
            fields=[
                ('client_ID', models.CharField(serialize=False, max_length=16, primary_key=True)),
                ('client_NAME', models.TextField()),
                ('client_GENDER', models.CharField(max_length=1, choices=[('M', '男性'), ('F', '女性')])),
                ('client_PHONE', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='client_pd',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('client_ID', models.FloatField(verbose_name=client.models.client_info)),
                ('zft', models.BooleanField(verbose_name='智付通')),
            ],
        ),
        migrations.AddField(
            model_name='client_balance',
            name='client_ID',
            field=models.ForeignKey(to='client.client_info'),
        ),
    ]
