# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-12-01 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myob', '0002_change_companyfiletoken_relation'),
    ]

    operations = [
        migrations.AddField(
            model_name='myobcompanyfile',
            name='authenticated',
            field=models.BooleanField(default=False),
        ),
    ]