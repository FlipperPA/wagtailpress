# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import wagtail.wagtailimages.blocks
import datetime
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailcore', '0019_verbose_names_cleanup'),
    ]

    operations = [
        migrations.CreateModel(
            name='WTPage',
            fields=[
                ('page_ptr', models.OneToOneField(to='wagtailcore.Page', auto_created=True, parent_link=True, primary_key=True, serialize=False)),
                ('content', wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('url', wagtail.wagtailcore.blocks.URLBlock()), ('code', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('python', 'Python'), ('bash', 'Bash/Shell'), ('html', 'HTML'), ('css', 'CSS'), ('scss', 'SCSS'), ('js', 'JavaScript')])), ('code', wagtail.wagtailcore.blocks.TextBlock()))))))),
                ('modified', models.DateTimeField(null=True, verbose_name='Post Modified')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='WTPost',
            fields=[
                ('page_ptr', models.OneToOneField(to='wagtailcore.Page', auto_created=True, parent_link=True, primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Post Date')),
                ('excerpt', models.CharField(max_length=250)),
                ('content', wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('url', wagtail.wagtailcore.blocks.URLBlock()), ('code', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('python', 'Python'), ('bash', 'Bash/Shell'), ('html', 'HTML'), ('css', 'CSS'), ('scss', 'SCSS'), ('js', 'JavaScript')])), ('code', wagtail.wagtailcore.blocks.TextBlock()))))))),
                ('modified', models.DateTimeField(null=True, verbose_name='Post Modified')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='author')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
