# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-18 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='webapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('email', models.TextField(max_length=20)),
                ('phone', models.IntegerField(max_length=20)),
                ('city', models.CharField(max_length=15)),
                ('profession', models.CharField(max_length=15)),
            ],
        ),
    ]
