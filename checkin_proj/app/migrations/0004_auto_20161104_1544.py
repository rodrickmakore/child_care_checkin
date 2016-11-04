# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-04 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20161103_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='checked_in',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='childstatus',
            name='status',
            field=models.CharField(choices=[('i', 'Check-In'), ('o', 'Check-Out')], max_length=1),
        ),
    ]