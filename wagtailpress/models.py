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
from wagtail.wagtailsnippets.models import register_snippet

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase

from .blocks import CodeBlock


class WPPageTag(TaggedItemBase):
    """
    Base class for storing tags for Pages and Posts.
    """
    content_object = ParentalKey('wagtailpress.WPPage', related_name='tagged_items')


@register_snippet
class Category(models.Model):
    """
    Base class for storing categories for Posts.
    """
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=255, blank=True)

    panels = [
        FieldPanel('name'),
    ]

    def __str__(self):
        return self.name


class WPPage(Page):
    """
    This class will hold pages, similar to WordPress' post_type of 'page'.
    Posts will inherit from this class, adding additional fields needed.
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
    tags = ClusterTaggableManager(through=WPPageTag, blank=True)
    modified = models.DateTimeField("Page Modified", null=True)

    search_fields = Page.search_fields + (
        index.SearchField('title'),
        index.SearchField('content'),
    )

    content_panels = Page.content_panels + [
        FieldPanel('tags'),
        StreamFieldPanel('content'),
    ]

    def save(self, *args, **kwargs):
        self.modified = timezone.now()
        super(WPPage, self).save(*args, **kwargs)

    def __str__(self):
        return 'ID %s: %s' % (str(self.pk), self.title)


class WPPost(WPPage):
    """
    This class will hold blog posts, similar to WordPress' post_type of 'post'.
    """
    
    class Meta:
        verbose_name = "Post"

    date = models.DateField("Post Date", default=date.today)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='author', on_delete=models.SET_NULL)
    categories = models.ManyToManyField(
        Category,
        blank=True,
    )
    excerpt = models.CharField(
        max_length=250,
        blank=True,
    )

    search_fields = WPPage.search_fields + (
        index.SearchField('title'),
        index.SearchField('excerpt'),
        index.SearchField('content'),
    )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('author'),
        FieldPanel('categories'),
        FieldPanel('excerpt'),
        FieldPanel('tags'),
        StreamFieldPanel('content'),
    ]

    def __str__(self):
        return 'ID %s: %s' % (str(self.pk), self.title)


"""
class BlogIndexPage(Page):
    excerpt = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('excerpt', classname="full")
    ]
"""
