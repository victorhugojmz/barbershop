# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-30 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('cita_id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_cita', models.DateField(verbose_name='Fecha')),
                ('fecha_creacion_cita', models.DateTimeField(auto_now_add=True, null=True)),
                ('nombre_cliente', models.CharField(max_length=150)),
                ('telefono_cliente', models.CharField(max_length=20)),
                ('direccion', models.CharField(blank=True, max_length=120, null=True)),
                ('hora_cita', models.TimeField(verbose_name='Hora')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='cita',
            unique_together=set([('fecha_cita', 'hora_cita')]),
        ),
    ]
