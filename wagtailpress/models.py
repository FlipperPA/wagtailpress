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


class WTPage(Page):
    """
    This class will hold pages, similar to WordPress' post_type of 'page'.
    """
    
    class Meta:
        verbose_name = "Page"

    content = StreamField([
        ('heading', CharBlock(classname="full title")),
        ('paragraph', TextBlock()),
        ('image', ImageChooserBlock()),
        ('url', URLBlock()),
        ('code', CodeBlock()),
    ])
    modified = models.DateTimeField("Page Modified", null=True)

    search_fields = Page.search_fields + (
        index.SearchField('content'),
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    def save(self, *args, **kwargs):
        self.modified = timezone.now()
        super(WTPage, self).save(*args, **kwargs)


class WTPost(WTPage):
    """
    This class will hold blog posts, similar to WordPress' post_type of 'post'.
    """
    
    class Meta:
        verbose_name = "Post"

    date = models.DateField("Post Date", default=date.today)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='author', on_delete=models.SET_NULL)
    excerpt = models.CharField(max_length=250)

    search_fields = WTPage.search_fields + (
        index.SearchField('excerpt'),
        index.SearchField('content'),
    )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('author'),
        FieldPanel('excerpt'),
        StreamFieldPanel('content'),
    ]


"""
class BlogIndexPage(Page):
    excerpt = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('excerpt', classname="full")
    ]
"""
