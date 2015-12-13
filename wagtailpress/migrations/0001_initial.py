# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import wagtail.wagtailimages.blocks
import modelcluster.contrib.taggit
import datetime
import django.db.models.deletion
import wagtail.wagtailcore.fields
import modelcluster.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0002_auto_20150616_2121'),
        ('wagtailcore', '0020_add_index_on_page_first_published_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='WPPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, serialize=False, primary_key=True, parent_link=True, to='wagtailcore.Page')),
                ('content', wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('url', wagtail.wagtailcore.blocks.URLBlock()), ('code', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('python', 'Python'), ('bash', 'Bash/Shell'), ('html', 'HTML'), ('css', 'CSS'), ('scss', 'SCSS'), ('js', 'JavaScript')])), ('code', wagtail.wagtailcore.blocks.TextBlock()))))))),
                ('modified', models.DateTimeField(verbose_name='Page Modified', null=True)),
            ],
            options={
                'verbose_name': 'Page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='WPPageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WPPost',
            fields=[
                ('wppage_ptr', models.OneToOneField(auto_created=True, serialize=False, primary_key=True, parent_link=True, to='wagtailpress.WPPage')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Post Date')),
                ('excerpt', models.CharField(max_length=250)),
                ('author', models.ForeignKey(related_name='author', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Post',
            },
            bases=('wagtailpress.wppage',),
        ),
        migrations.AddField(
            model_name='wppagetag',
            name='content_object',
            field=modelcluster.fields.ParentalKey(related_name='tagged_items', to='wagtailpress.WPPage'),
        ),
        migrations.AddField(
            model_name='wppagetag',
            name='tag',
            field=models.ForeignKey(related_name='wagtailpress_wppagetag_items', to='taggit.Tag'),
        ),
        migrations.AddField(
            model_name='wppage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(through='wagtailpress.WPPageTag', verbose_name='Tags', blank=True, to='taggit.Tag', help_text='A comma-separated list of tags.'),
        ),
    ]
