# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ticketsystem', '0003_auto_20160201_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='followup_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 1, 11, 44, 2, 765765)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 1, 11, 44, 2, 764876)),
        ),
    ]
