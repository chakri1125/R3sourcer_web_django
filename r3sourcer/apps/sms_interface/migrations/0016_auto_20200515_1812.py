# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-05-15 18:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sms_interface', '0015_auto_20200407_0622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smsmessage',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Company', verbose_name='Company'),
        ),
    ]
