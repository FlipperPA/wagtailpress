from datetime import date

from django.conf import settings
from django.db import models
from django.utils import timezone

from wagtail.wagtailcore.blocks import CharBlock, TextBlock, URLBlock
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsearch import index

from .blocks import CodeBlock


class Post(Page):
    date = models.DateField("Post Date", default=date.today)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='author')
    excerpt = models.CharField(max_length=250)
    content = StreamField([
        ('heading', CharBlock(classname="full title")),
        ('paragraph', TextBlock()),
        ('image', ImageChooserBlock()),
        ('url', URLBlock()),
        ('code', CodeBlock()),
    ])
    modified = models.DateTimeField("Post Modified", null=True)

    search_fields = Page.search_fields + (
        index.SearchField('excerpt'),
        index.SearchField('content'),
    )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('author'),
        FieldPanel('excerpt'),
        StreamFieldPanel('content'),
    ]

    def save(self, *args, **kwargs):
        self.modified = timezone.now()
        super(Post, self).save(*args, **kwargs)

class BlogIndexPage(Page):
    excerpt = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('excerpt', classname="full")
    ]
