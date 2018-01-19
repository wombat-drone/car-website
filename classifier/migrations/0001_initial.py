# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-18 23:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default='', max_length=200)),
            ],
            options={
                'db_table': 'car',
            },
        ),
        migrations.CreateModel(
            name='InputImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
                ('predictions1', models.CharField(default='', max_length=200)),
                ('predictions2', models.CharField(default='', max_length=200)),
                ('predictions3', models.CharField(default='', max_length=200)),
            ],
            options={
                'db_table': 'input_image',
            },
        ),
    ]
