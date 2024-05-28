# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-04-14 11:42
from __future__ import unicode_literals

import json
import os

from django.core.management import CommandError
from django.db import migrations


class Migration(migrations.Migration):

    def load_new_default_sms_templates_from_fixture(apps, schema_editor):
        DefaultSMSTemplate = apps.get_model("sms_interface", "DefaultSMSTemplate")
        Language = apps.get_model("core", "Language")
        sms_templates = []
        try:
            basepath = os.path.dirname(__file__)
            filepath = os.path.abspath(os.path.join(
                basepath, "..", "fixtures", "default_sms_template.json")
            )
            with open(filepath, 'r') as json_file:
                data = json.load(json_file)
                for el in data:
                    try:
                        template = el['fields']
                        lang = Language.objects.get(alpha_2=template['language'])
                        existing_template = DefaultSMSTemplate.objects.get(slug=template['slug'], language=lang)
                        # update only consent templates
                        # might be removed after deployment
                        if existing_template.slug == 'consent-sms-message':
                            existing_template.message_text_template = template['message_text_template']
                            existing_template.save()
                    except DefaultSMSTemplate.DoesNotExist:
                        obj = DefaultSMSTemplate(
                            name=template['name'],
                            slug=template['slug'],
                            message_text_template=template['message_text_template'],
                            reply_timeout=template['reply_timeout'],
                            delivery_timeout=template['delivery_timeout'],
                            language=lang)
                        sms_templates.append(obj)
                    except Language.DoesNotExist:
                        continue
            if len(sms_templates) > 0:
                DefaultSMSTemplate.objects.bulk_create(sms_templates)

        except Exception as e:
            raise CommandError(e)

    dependencies = [
        ('sms_interface', '0018_load_new_sms_templates'),
    ]

    operations = [
        # migrations.RunPython(load_new_default_sms_templates_from_fixture),
    ]
