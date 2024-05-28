# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-20 07:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    def propagate_default_sms_templates(apps, schema_editor):
        DefaultSMSTemplate = apps.get_model("sms_interface", "DefaultSMSTemplate")
        SMSTemplate = apps.get_model("sms_interface", "SMSTemplate")
        Company = apps.get_model("core", "Company")
        default_templates = DefaultSMSTemplate.objects.all()
        sms_templates = []
        for company in Company.objects.all():
            if company.type != 'master':
                continue

            for template in default_templates:
                obj = SMSTemplate(
                    name=template.name,
                    slug=template.slug,
                    message_text_template=template.message_text_template,
                    reply_timeout=template.reply_timeout,
                    delivery_timeout=template.delivery_timeout,
                    company_id=company.id)
                sms_templates.append(obj)
        SMSTemplate.objects.bulk_create(sms_templates)

    dependencies = [
        ('sms_interface', '0010_auto_20200219_2008'),
    ]

    operations = [
        # migrations.RunPython(propagate_default_sms_templates),
    ]