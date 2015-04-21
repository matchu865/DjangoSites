# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Golfer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course', models.CharField(max_length=200)),
                ('score', models.IntegerField(default=72)),
                ('gir', models.IntegerField(default=12)),
                ('putts', models.IntegerField(default=36)),
                ('fairways', models.IntegerField(default=12)),
                ('golfer', models.ForeignKey(to='golfers.Golfer')),
            ],
        ),
    ]
