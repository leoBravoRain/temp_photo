# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-15 20:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('photo', models.ImageField(upload_to='imagenes/photo')),
            ],
        ),
    ]