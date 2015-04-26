# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('golfers', '0005_auto_20150426_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golfer',
            name='age',
            field=models.IntegerField(default=30, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='round',
            name='fairways',
            field=models.IntegerField(default=12, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(18)]),
        ),
        migrations.AlterField(
            model_name='round',
            name='gir',
            field=models.IntegerField(default=12, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(18)]),
        ),
        migrations.AlterField(
            model_name='round',
            name='putts',
            field=models.IntegerField(default=36, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='round',
            name='score',
            field=models.IntegerField(default=72, validators=[django.core.validators.MinValueValidator(50)]),
        ),
    ]
