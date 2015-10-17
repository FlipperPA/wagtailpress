# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpress', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wtpage',
            options={'verbose_name': 'Page'},
        ),
        migrations.AlterModelOptions(
            name='wtpost',
            options={'verbose_name': 'Post'},
        ),
    ]
