# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.blocks
import datetime
import wagtail.wagtailcore.fields
from django.conf import settings
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0020_add_index_on_page_first_published_at'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WTPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, auto_created=True, primary_key=True, to='wagtailcore.Page', parent_link=True)),
                ('content', wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('url', wagtail.wagtailcore.blocks.URLBlock()), ('code', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('python', 'Python'), ('bash', 'Bash/Shell'), ('html', 'HTML'), ('css', 'CSS'), ('scss', 'SCSS'), ('js', 'JavaScript')])), ('code', wagtail.wagtailcore.blocks.TextBlock()))))))),
                ('modified', models.DateTimeField(verbose_name='Page Modified', null=True)),
            ],
            options={
                'verbose_name': 'Page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='WTPost',
            fields=[
                ('wtpage_ptr', models.OneToOneField(serialize=False, auto_created=True, primary_key=True, to='wagtailpress.WTPage', parent_link=True)),
                ('date', models.DateField(verbose_name='Post Date', default=datetime.date.today)),
                ('excerpt', models.CharField(max_length=250)),
                ('author', models.ForeignKey(related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
            },
            bases=('wagtailpress.wtpage',),
        ),
    ]
