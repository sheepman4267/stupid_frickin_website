from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail.images import get_image_model
from wagtail.blocks import RichTextBlock
from wagtail.images.blocks import ImageBlock
from core.blocks import FeaturedPageBlock, RecentPostsBlock
# Create your models here.


class StandardBlockPage(Page):
    body = StreamField(
        block_types=[
            ('rich_text', RichTextBlock()),
            ('image', ImageBlock()),
            ('featured_page', FeaturedPageBlock()),
            ('recent_posts', RecentPostsBlock(max_num=1)),
        ]
    )
    featured_image = models.ForeignKey(
        to=get_image_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
    )
    summary = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('featured_image'),
        FieldPanel('body'),
        FieldPanel('summary'),
    ]

    def get_posts(self):
        return PostPage.objects.live().descendant_of(self).order_by('last_published_at')


class PostPage(StandardBlockPage):
    parent_page_types = ['core.StandardBlockPage']
    template = 'core/standard_block_page.html'

    class Meta:
        verbose_name = 'Post'
