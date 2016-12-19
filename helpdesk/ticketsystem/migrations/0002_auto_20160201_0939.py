# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ticketsystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='followup_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 1, 9, 39, 41, 439837)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 1, 9, 39, 41, 437805)),
        ),
    ]
