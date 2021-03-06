# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-08 21:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('i', 'Check-In'), ('o', 'Check-Out')], max_length=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('parent_name', models.CharField(max_length=100)),
                ('child_name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=4)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='childreport',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.CustomerProfile'),
        ),
    ]
