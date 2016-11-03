# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-03 20:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20161103_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]