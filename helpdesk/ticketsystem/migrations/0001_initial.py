# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('followupnote', models.CharField(max_length=1000)),
                ('followup_date', models.DateTimeField(default=datetime.datetime(2016, 2, 1, 8, 58, 16, 297346))),
                ('assigned_user', models.ForeignKey(related_name='assigned_user', to='userprofile.UserProfile')),
                ('followup_user', models.ForeignKey(related_name='followup_user', to='userprofile.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': '\xd6ncelik',
                'verbose_name_plural': '\xd6ncelikler',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('department', models.ForeignKey(to='userprofile.Department')),
            ],
            options={
                'verbose_name': 'Hizmet',
                'verbose_name_plural': 'Hizmetler',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': '\u0130\u015f durum',
                'verbose_name_plural': '\u0130\u015f durumlar\u0131',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(max_length=1000)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2016, 2, 1, 8, 58, 16, 296461))),
                ('creator', models.ForeignKey(to='userprofile.UserProfile')),
                ('department', models.ForeignKey(to='userprofile.Department')),
                ('priority', models.ForeignKey(to='ticketsystem.Priority')),
                ('product', models.ForeignKey(to='ticketsystem.Product')),
                ('status', models.ForeignKey(to='ticketsystem.Status')),
            ],
            options={
                'verbose_name': '\u0130\u015f',
                'verbose_name_plural': '\u0130\u015fler',
            },
        ),
        migrations.AddField(
            model_name='followup',
            name='ticket',
            field=models.ForeignKey(to='ticketsystem.Ticket'),
        ),
    ]
