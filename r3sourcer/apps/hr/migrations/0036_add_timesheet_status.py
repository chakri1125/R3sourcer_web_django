# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-22 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0035_timesheet_sync_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheet',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'New'), (1, 'Check pending'), (2, 'Check confirmed'), (3, 'Check failed'), (4, 'Submit pending'), (5, 'Pending approval'), (6, 'Supervisor modified'), (7, 'Approved')], default=0, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='timesheet',
            name='supervisor_modified',
            field=models.BooleanField(default=False, verbose_name='Supervisor modified shift'),
        ),
    ]
