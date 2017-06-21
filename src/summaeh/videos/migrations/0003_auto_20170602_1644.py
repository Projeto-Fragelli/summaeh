# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-02 19:44
from __future__ import unicode_literals

from django.db import migrations, models
import summaeh.videos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20170505_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='link',
            field=models.URLField(help_text='Link do vídeo no Youtube (ex.: https://youtube.com/...)', validators=[summaeh.videos.validators.is_youtube_video], verbose_name='Link'),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='like',
            name='type',
        ),
    ]