# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-11-28 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twilio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twilioaccount',
            name='created_at',
            field=models.DateTimeField(editable=False, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='twiliocredential',
            name='created_at',
            field=models.DateTimeField(editable=False, verbose_name='Created at'),
        ),
    ]