# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-11 10:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_auto_20180111_1625'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-created_at']},
        ),
    ]
