# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-08-01 11:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0061_companyworkflownode_order'),
        ('login', '0002_updated_redirect_upl_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='tokenlogin',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Role', verbose_name='User role'),
        ),
    ]