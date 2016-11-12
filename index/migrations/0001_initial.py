# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-12 07:37
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_barbero', models.CharField(max_length=60)),
                ('cuenta_twitter_barbero', models.CharField(max_length=30)),
                ('cuenta_facebook_barbero', models.CharField(max_length=30)),
                ('descripcion_barbero', models.TextField(max_length=350)),
                ('fotografia_barbero', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('titulo_imagen', models.CharField(max_length=100)),
                ('imagen', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=150)),
                ('tipo_producto', models.CharField(max_length=50)),
                ('marca_producto', models.CharField(max_length=50)),
                ('precio_unitario_producto', models.IntegerField(default=0)),
                ('stock_producto', models.IntegerField(default=0)),
                ('imagen_producto', models.FileField(upload_to=b'')),
                ('descripcion_producto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_servicio', models.CharField(default='Corte de pelo', max_length=30)),
                ('tipo_servicio', models.CharField(max_length=50)),
                ('imagen_corte', models.CharField(max_length=200)),
                ('precio_servicio', models.IntegerField()),
            ],
        ),
    ]
