# Generated by Django 2.0.13 on 2023-10-26 13:18

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0030_add_subscription_statuses'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='stripecountryaccount',
        #     name='id',
        #     field=models.AutoField(auto_created=True, default=builtins.dir, primary_key=True, serialize=False, verbose_name='ID'),
        #     preserve_default=False,
        # ),
        migrations.AlterField(
            model_name='subscriptiontype',
            name='step_change_val',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
