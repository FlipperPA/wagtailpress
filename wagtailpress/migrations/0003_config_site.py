# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 22:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('wagtailpress', '0002_auto_20160228_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='site', to='wagtailcore.Site'),
        ),
    ]
