# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('golfers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='round_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 21, 20, 4, 24, 761147, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
    ]
