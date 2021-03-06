# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-05 14:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='autores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='lectores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='titulos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=90)),
                ('fecha', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('puntuacion', models.PositiveIntegerField(blank=True, null=True)),
                ('isbn', models.CharField(max_length=75)),
                ('portada', models.ImageField(blank=True, upload_to='imagenes')),
                ('autor', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='libros.autores')),
                ('lector', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='libros.lectores')),
            ],
        ),
    ]
