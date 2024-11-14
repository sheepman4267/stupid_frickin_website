from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField

from wagtail.models import Page

from core.blocks import FeaturedPageBlock
from core.models import PostPage


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('featured_projects'),
    ]

    featured_projects = StreamField(
        block_types=[
            ('featured_page', FeaturedPageBlock(heading='Featured Project')),
        ],
        null=True,
        blank=True,
    )

    def get_posts(self):
        return PostPage.objects.live().descendant_of(self).order_by('last_published_at')[:5]
