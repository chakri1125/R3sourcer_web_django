# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-04-10 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0108_auto_20200410_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccountlayout',
            name='slug',
            field=models.SlugField(max_length=32, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bankaccountlayout',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
