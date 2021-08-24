from django.db import models

# Create your models here.
from django.db import models
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
# Create your models here.


class LearninPage(Page):
    """Landing page for about us"""
    template = "learning/learning_site.html"
    
    body = StreamField(
        [
            ("heading", blocks.CharBlock(form_classname="Full Title")),
            ("Paragraph", blocks.RichTextBlock()),
            ("Immage", ImageChooserBlock()),
        ]
    )
    
    content_panels = Page.content_panels + [
        StreamFieldPanel("body")
    ]