# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-06-05 08:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DraftPrintJob',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.IntegerField(choices=[(0, 'PENDING'), (1, 'IN_PROGRESS'), (2, 'DONE'), (3, 'INVALID')])),
                ('worker', models.CharField(blank=True, max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FinalPrintJob',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.IntegerField(choices=[(0, 'PENDING'), (1, 'IN_PROGRESS'), (2, 'DONE'), (3, 'INVALID')])),
                ('worker', models.CharField(blank=True, max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PrintedDraftDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.FilePathField(match='*.pdf', recursive=True)),
                ('print_count', models.PositiveIntegerField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='print_job_queue.DraftPrintJob')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PrintedFinalDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.FilePathField(match='*.pdf', recursive=True)),
                ('print_count', models.PositiveIntegerField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='print_job_queue.FinalPrintJob')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]