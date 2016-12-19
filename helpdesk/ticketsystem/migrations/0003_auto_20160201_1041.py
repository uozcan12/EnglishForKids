# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ticketsystem', '0002_auto_20160201_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='followup_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 1, 10, 41, 6, 989595)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 1, 10, 41, 6, 988586)),
        ),
    ]
