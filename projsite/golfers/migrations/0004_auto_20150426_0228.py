# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('golfers', '0003_auto_20150421_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golfer',
            name='age',
            field=models.CharField(default=30, max_length=3),
        ),
    ]
