# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-09 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0015_remove_video_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='description',
            field=models.TextField(default='', max_length=500, verbose_name='Descrição'),
        ),
    ]
