# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-06-25 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('print_job_queue', '0002_auto_20220618_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='draftprintjob',
            name='group',
            field=models.CharField(default='default_group', max_length=25),
        ),
        migrations.AddField(
            model_name='finalprintjob',
            name='group',
            field=models.CharField(default='default_group', max_length=25),
        ),
    ]