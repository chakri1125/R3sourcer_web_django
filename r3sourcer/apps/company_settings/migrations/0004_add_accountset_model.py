# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-10 12:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

from r3sourcer.apps.company_settings.models import MYOBAccount


def create_myob_accounts(apps, schema_editor):
    MYOBAccount.objects.create(number='1-1000',
                               name='Test Expense Account',
                               type='expense')
    MYOBAccount.objects.create(number='2-2000',
                               name='Test Income Account',
                               type='income')


class Migration(migrations.Migration):

    dependencies = [
        ('company_settings', '0003_add_companysettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MYOBAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=63)),
                ('name', models.CharField(max_length=63)),
                ('type', models.CharField(max_length=63)),
            ],
        ),
        migrations.AddField(
            model_name='accountset',
            name='candidate_superannuation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidate_superannuation', to='company_settings.MYOBAccount'),
        ),
        migrations.AddField(
            model_name='accountset',
            name='candidate_wages',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidate_wages', to='company_settings.MYOBAccount'),
        ),
        migrations.AddField(
            model_name='accountset',
            name='company_client_gst',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_client_gst', to='company_settings.MYOBAccount'),
        ),
        migrations.AddField(
            model_name='accountset',
            name='company_client_labour_hire',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_client_labour_hire', to='company_settings.MYOBAccount'),
        ),
        migrations.AddField(
            model_name='accountset',
            name='subcontractor_contract_work',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcontractor_contract_work', to='company_settings.MYOBAccount'),
        ),
        migrations.AddField(
            model_name='accountset',
            name='subcontractor_gst',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcontractor_gst', to='company_settings.MYOBAccount'),
        ),
        migrations.AddField(
            model_name='companysettings',
            name='account_set',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_settings', to='company_settings.AccountSet'),
        ),
    ]