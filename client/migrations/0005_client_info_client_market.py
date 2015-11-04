# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_market'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_info',
            name='client_MARKET',
            field=models.ForeignKey(to='client.market', default=''),
            preserve_default=False,
        ),
    ]
