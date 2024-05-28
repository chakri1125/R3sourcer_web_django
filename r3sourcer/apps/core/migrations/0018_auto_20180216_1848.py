# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-02-16 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20180208_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='companycontact',
            name='message_by_email',
            field=models.BooleanField(default=True, verbose_name='By E-Mail'),
        ),
        migrations.AddField(
            model_name='companycontact',
            name='message_by_sms',
            field=models.BooleanField(default=True, verbose_name='By SMS'),
        ),
    ]