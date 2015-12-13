# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpress', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wtpost',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='author', on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
