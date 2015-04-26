# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('golfers', '0004_auto_20150426_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golfer',
            name='age',
            field=models.IntegerField(default=30),
        ),
    ]
