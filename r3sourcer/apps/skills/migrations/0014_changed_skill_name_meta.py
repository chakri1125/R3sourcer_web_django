# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-09-03 09:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0013_remove_skill_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skillname',
            options={'verbose_name': 'Skill Name', 'verbose_name_plural': 'Skill Name'},
        ),
    ]
