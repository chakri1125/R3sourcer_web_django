# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-06-29 12:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0011_merge_20180627_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skillraterel',
            name='candidate_skill',
        ),
        migrations.RemoveField(
            model_name='skillraterel',
            name='hourly_rate',
        ),
        migrations.DeleteModel(
            name='SkillRateRel',
        ),
    ]