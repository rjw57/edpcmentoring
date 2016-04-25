# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 19:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('last_inactive_on', models.DateField(blank=True, null=True)),
                ('arrived_on', models.DateField(auto_now_add=True)),
                ('first_names', models.CharField(blank=True, default='', max_length=100)),
                ('division', models.CharField(blank=True, choices=[('A', 'Energy, Fluids and Turbomachinery'), ('B', 'Electrical Engineering'), ('C', 'Mechanics, Materials and Design'), ('D', 'Civil Engineering'), ('E', 'Manufacturing and Management'), ('F', 'Information Engineering'), ('', 'No Division')], default='', max_length=1)),
                ('research_group', models.CharField(blank=True, default='', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cued_member', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('S', 'Staff'), ('P', 'Postgrad'), ('V', 'Visitor')], max_length=1)),
                ('start_on', models.DateField()),
                ('end_on', models.DateField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statuses', to='cuedmembers.Member')),
            ],
            options={
                'verbose_name_plural': 'Statuses',
            },
        ),
    ]
