# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 16:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mentoring', '0002_auto_20160424_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('held_on', models.DateField()),
                ('approximate_duration', models.DurationField()),
                ('relationship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentoring.MentorshipRelationship')),
            ],
        ),
    ]
