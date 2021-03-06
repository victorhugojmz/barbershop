# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-27 23:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barbero',
            fields=[
                ('id_barbero', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_barbero', models.CharField(max_length=60)),
                ('cuenta_twitter_barbero', models.CharField(blank=True, max_length=30, null=True)),
                ('cuenta_facebook_barbero', models.CharField(blank=True, max_length=30, null=True)),
                ('descripcion_barbero', models.TextField(max_length=350)),
                ('fotografia_barbero', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id_imagen', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('titulo_imagen', models.CharField(blank=True, max_length=100, null=True)),
                ('imagen', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_servicio', models.CharField(default='Corte de pelo', max_length=30)),
                ('tipo_servicio', models.CharField(max_length=50)),
                ('imagen_corte', models.CharField(max_length=200)),
                ('precio_servicio', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
