# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-23 15:04
from __future__ import unicode_literals

from datetime import timedelta
from django.db import migrations
from django.db.models import F
from django.utils import timezone
from model_utils import Choices


def update_timesheet_status(apps, schema):
    """
    Update status of existing timesheet in database.

    :type schema: django.db.backends.base.schema.BaseDatabaseSchemaEditor
    :type apps: django.apps.registry.Apps
    """
    STATUS_CHOICES = Choices(
        (0, 'new', 'new'),
        (1, 'check_pending', 'check_pending'),
        (2, 'check_confirmed', 'check_confirmed'),
        (3, 'check_failed', 'check_failed'),
        (4, 'submit_pending', 'submit_pending'),
        (5, 'approval_pending', 'approval_pending'),
        (6, 'modified', 'modified'),
        (7, 'approved', 'approved'),
    )

    TimeSheetModel = apps.get_model('hr', 'TimeSheet')

    pre_shift_sms_delta = F('job_offer__shift__date__job__jobsite__'
                            'master_company__company_settings__pre_shift_sms_delta')

    for time_sheet in TimeSheetModel.objects.annotate(pre_shift_sms_delta=pre_shift_sms_delta):
        if time_sheet.supervisor_approved_at is not None:
            if time_sheet.supervisor_modified and time_sheet.status != STATUS_CHOICES.approved:
                time_sheet.status = STATUS_CHOICES.modified
            else:
                time_sheet.status = STATUS_CHOICES.approved

        elif time_sheet.candidate_submitted_at is not None:
            time_sheet.status = STATUS_CHOICES.approval_pending

        elif time_sheet.going_to_work_confirmation:
            if time_sheet.shift_started_at <= timezone.localtime():
                time_sheet.status = STATUS_CHOICES.submit_pending
            else:
                time_sheet.status = STATUS_CHOICES.check_confirmed

        elif time_sheet.going_to_work_confirmation is None:
            pre_shift_sms_delta = time_sheet.pre_shift_sms_delta  # annotated field
            going_eta = time_sheet.shift_started_at - timedelta(minutes=pre_shift_sms_delta)
            if going_eta <= timezone.localtime():
                time_sheet.status = STATUS_CHOICES.check_pending

        elif not time_sheet.going_to_work_confirmation:
            time_sheet.status = STATUS_CHOICES.check_failed
        time_sheet.save(update_fields=['status'])


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0036_add_timesheet_status'),
    ]

    operations = [
        migrations.RunPython(update_timesheet_status, migrations.RunPython.noop)
    ]