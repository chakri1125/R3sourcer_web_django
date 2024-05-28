# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-08-24 09:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0034_auto_20210824_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worktype',
            name='skill',
            field=models.ForeignKey(blank=True, help_text='Fill in this field only for Company skill activities', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_types', to='skills.Skill', verbose_name='Skill'),
        ),
        migrations.AlterField(
            model_name='worktype',
            name='skill_name',
            field=models.ForeignKey(blank=True, help_text='Fill in this field only for System skill activities', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_types', to='skills.SkillName', verbose_name='Skill Name'),
        ),
    ]
