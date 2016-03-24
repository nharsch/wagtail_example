from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsearch import index


class BlogPage(Page):
    # we can use django fields
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    # or wagtail fields
    body = RichTextField(blank=True)
    search_fields = Page.search_fields + (
        index.SearchField('into'),
        index.SearchField('body'),
    )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full")
    ]


