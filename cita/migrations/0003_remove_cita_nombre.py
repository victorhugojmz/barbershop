# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-10 20:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cita', '0002_auto_20161110_0110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cita',
            name='nombre',
        ),
    ]
