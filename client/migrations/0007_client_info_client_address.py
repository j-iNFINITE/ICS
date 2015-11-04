# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_client_info_client_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_info',
            name='client_ADDRESS',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
