# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-01-29 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silver', '0049_auto_20190129_2139'),
        ('silver_cpay', '0004_auto_20190129_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment_request',
            name='invoice_ids',
        ),
        migrations.RemoveField(
            model_name='payment_request',
            name='proforma_ids',
        ),
        migrations.AddField(
            model_name='payment_request',
            name='invoices',
            field=models.ManyToManyField(related_name='invoice_payment_requests', to='silver.Invoice'),
        ),
        migrations.AddField(
            model_name='payment_request',
            name='proformas',
            field=models.ManyToManyField(related_name='proforma_payment_requests', to='silver.Proforma'),
        ),
    ]
