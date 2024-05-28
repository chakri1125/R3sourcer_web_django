# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-11-28 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acceptance_tests', '0010_acceptancetestrelationship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acceptancetest',
            name='created_at',
            field=models.DateTimeField(editable=False, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='acceptancetestanswer',
            name='created_at',
            field=models.DateTimeField(editable=False, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='acceptancetestindustry',
            name='created_at',
            field=models.DateTimeField(editable=False, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='acceptancetestquestion',
            name='created_at',
            field=models.DateTimeField(editable=False, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='acceptancetestrelationship',
            name='created_at',
            field=models.DateTimeField(editable=False, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='acceptancetestskill',
            name='created_at',
            field=models.DateTimeField(editable=False, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='acceptancetesttag',
            name='created_at',
            field=models.DateTimeField(editable=False, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='acceptancetestworkflownode',
            name='created_at',
            field=models.DateTimeField(editable=False, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='workflowobjectanswer',
            name='created_at',
            field=models.DateTimeField(editable=False, verbose_name='Created at'),
        ),
    ]