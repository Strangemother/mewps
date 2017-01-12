from __future__ import absolute_import, unicode_literals

from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, \
     InlinePanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock


class H1Block(blocks.CharBlock):
    class Meta:
        template = 'blocks/h1.html'


class HomePage(Page):

    body = RichTextField(null=True, blank=True)
    date = models.DateField("Post date", null=True, blank=True)

    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body', classname="full"),
        InlinePanel('related_links', label="Related links"),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        ImageChooserPanel('feed_image'),
        # StreamFieldPanel('stream_field'),
    ]


class HomePageRelatedLink(Orderable):
    page = ParentalKey(HomePage, related_name='related_links')
    name = models.CharField(max_length=255)
    url = models.URLField()

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
    ]



class StandardPage(Page):

    page_content = StreamField([
        ('heading_h1', H1Block(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], null=True, blank=True)

    plain_content = RichTextField(null=True, blank=True)
    date = models.DateField("Post date", null=True, blank=True)

    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Search index configuration

    search_fields = Page.search_fields + [
        index.FilterField('date'),
        index.SearchField('plain_content'),
    ]


    # Editor panels configuration

    content_panels = Page.content_panels + [
        StreamFieldPanel('page_content'),
        FieldPanel('date'),
        FieldPanel('plain_content', classname="full"),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        ImageChooserPanel('feed_image'),
        InlinePanel('related_links', label="Related links"),
    ]


class StandardPageRelatedLink(Orderable):
    page = ParentalKey(StandardPage, related_name='related_links')
    name = models.CharField(max_length=255)
    url = models.URLField()

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
    ]
