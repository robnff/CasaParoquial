# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20160528_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membro',
            name='data_casamento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='membro',
            name='data_nasc',
            field=models.DateField(null=True),
        ),
    ]
