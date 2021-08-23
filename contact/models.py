from django.db import models
from wagtailstreamforms.blocks import WagtailFormBlock
from wagtailstreamforms.models.abstract import AbstractFormSetting

from django.utils.translation import gettext_lazy as _

from wagtail.core import blocks
from wagtail.core.models import Page

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField

# Create your models here.
class ContactPage(Page):
    intro = RichTextField(blank=True)
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('form', WagtailFormBlock()),
    ])
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        StreamFieldPanel('body'),
    ]


class AdvancedFormSetting(AbstractFormSetting):
    to_address = models.EmailField()
