# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 12:51
from __future__ import unicode_literals

from django.conf import settings
from django.core.management import call_command
from django.db import migrations, models
import django.db.models.deletion

def load_dept_structure(apps, schema_editor):
    call_command('loaddata', 'cuedmembers/divisions_and_research_groups.json')

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('letter', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_names', models.CharField(blank=True, default='', max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResearchGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='research_groups', to='cuedmembers.Division')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='research_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='cuedmembers.ResearchGroup'),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cued_member', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RunPython(load_dept_structure),
    ]
