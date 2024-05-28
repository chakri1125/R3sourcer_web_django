# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-09-10 06:16
from __future__ import unicode_literals

from django.db import migrations, models


def migrate_job_offer_smses(apps, schema_editor):
    JobOffer = apps.get_model('hr', 'JobOffer')
    JobOfferSMS = apps.get_model('hr', 'JobOfferSMS')

    job_offers = JobOffer.objects.filter(
        models.Q(offer_sent_by_sms__isnull=False) |
        models.Q(reply_received_by_sms__isnull=False)
    )

    for job_offer in job_offers:
        JobOfferSMS.objects.get_or_create(
            job_offer=job_offer,
            offer_sent_by_sms=job_offer.offer_sent_by_sms,
            reply_received_by_sms=job_offer.reply_received_by_sms,
        )


def reverse_job_offer_smses(apps, schema_editor):
    JobOffer = apps.get_model('hr', 'JobOffer')

    job_offers = JobOffer.objects.filter(job_offer_smses__isnull=False)

    for job_offer in job_offers:
        job_offer_sms = job_offer.job_offer_smses.first()
        job_offer.offer_sent_by_sms = job_offer_sms.offer_sent_by_sms
        job_offer.reply_received_by_sms = job_offer_sms.reply_received_by_sms
        job_offer.save(update_fields=['offer_sent_by_sms', 'reply_received_by_sms'])


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0029_joboffersms'),
    ]

    operations = [
        migrations.RunPython(migrate_job_offer_smses, reverse_job_offer_smses)
    ]
