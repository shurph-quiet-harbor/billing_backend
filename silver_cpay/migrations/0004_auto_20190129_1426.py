# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-01-29 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silver_cpay', '0003_auto_20190129_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='status',
            field=models.CharField(choices=[(b'success', b'success'), (b'fail', b'fail'), (b'invalid_data', b'invalid_data')], max_length=9),
        ),
    ]
