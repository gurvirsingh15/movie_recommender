# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-04 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_recommender', '0002_auto_20190104_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='titles',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
