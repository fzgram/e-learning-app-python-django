# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 17:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils import timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_delete_addstudents'),
    ]

    operations = [
        migrations.AddField(
            model_name='textblock',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=timezone.make_aware(datetime.datetime(2016, 4, 24, 17, 40, 54, 345815))),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ytlink',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=timezone.make_aware(datetime.datetime(2016, 4, 24, 17, 41, 11, 187939))),
            preserve_default=False,
        ),
    ]
