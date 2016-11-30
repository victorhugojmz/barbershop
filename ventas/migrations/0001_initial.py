# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-27 23:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0001_initial'),
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_venta', models.DateTimeField(auto_now_add=True, verbose_name='Creacion')),
                ('total_venta', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='VentaProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=6)),
                ('id_venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.Venta')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='VentaServicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=6)),
                ('id_venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.Venta')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Servicio')),
            ],
        ),
    ]