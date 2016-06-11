# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-29 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0007_auto_20160528_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='membro',
            name='escolaridade',
            field=models.CharField(blank=True, choices=[('sem', 'Não tem'), ('fund', 'Fundamental'), ('medio', 'Médio'), ('super', 'Superior'), ('pos', 'Pós-graduado')], max_length=5),
        ),
    ]