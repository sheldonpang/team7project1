# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default=datetime.datetime(2016, 1, 17, 18, 33, 56, 239648, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
