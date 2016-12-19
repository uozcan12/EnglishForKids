# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'Birim', 'verbose_name_plural': 'Birimler'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Kullan\u0131c\u0131 Profili', 'verbose_name_plural': 'Kullan\u0131c\u0131 Profilleri'},
        ),
        migrations.RenameField(
            model_name='department',
            old_name='depadmin',
            new_name='manager',
        ),
        migrations.RenameField(
            model_name='department',
            old_name='ad',
            new_name='name',
        ),
    ]
