# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('golfers', '0002_round_round_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_name', models.CharField(max_length=60)),
                ('par', models.IntegerField(default=72)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=2)),
            ],
        ),
        migrations.AlterField(
            model_name='round',
            name='course',
            field=models.ForeignKey(to='golfers.Course'),
        ),
    ]
