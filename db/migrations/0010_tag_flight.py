# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-20 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0009_truncate_tags_and_markers'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='flight',
            field=models.ManyToManyField(to='db.Flight'),
        ),
    ]
