# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-22 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0002_auto_20180119_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='body_style',
            field=models.CharField(default='N/A', max_length=15),
        ),
        migrations.AddField(
            model_name='car',
            name='make',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='car',
            name='year',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AlterField(
            model_name='car',
            name='label',
            field=models.CharField(default='', max_length=200),
        ),
    ]
