# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-06-08 11:41
from __future__ import unicode_literals

from django.db import migrations
from r3sourcer.apps.core.models import Role, Company


def migrate_roles(apps, schema_editor):
    RoleObj = apps.get_model("core", "Role")
    CompanyContactRelationship = apps.get_model("core", "CompanyContactRelationship")
    CandidateContact = apps.get_model("candidate", "CandidateContact")

    for company_contact_rel in CompanyContactRelationship.objects.all():
        role = Role.ROLE_NAMES.client
        if company_contact_rel.company.type == Company.COMPANY_TYPES.master:
            role = Role.ROLE_NAMES.manager

        user = company_contact_rel.company_contact.contact.user
        if user and not user.role.filter(name=role).exists():
            user.role.add(RoleObj.objects.create(name=role))

    for candidate_contact in CandidateContact.objects.all():
        user = candidate_contact.contact.user
        if user and not user.role.filter(name=role).exists():
            user.role.add(RoleObj.objects.create(name=Role.ROLE_NAMES.candidate))


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_company_industry'),
    ]

    operations = [
        migrations.RunPython(migrate_roles, migrations.RunPython.noop)
    ]
