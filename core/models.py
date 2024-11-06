from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail.images import get_image_model
from wagtail.blocks import RichTextBlock
from wagtail.images.blocks import ImageBlock
# Create your models here.


class StandardBlockPage(Page):
    body = StreamField(
        block_types=[
            ('rich_text', RichTextBlock()),
            ('image', ImageBlock()),
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
