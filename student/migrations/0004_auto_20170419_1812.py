# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20170418_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], default='Male', max_length=6),
        ),
    ]
