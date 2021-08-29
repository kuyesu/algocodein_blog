from django.db import models
from django.db.models.fields.related import ForeignKey
from wagtail.admin.edit_handlers import MultiFieldPanel, ObjectList, PageChooserPanel
from wagtail.core.blocks.field_block import RichTextBlock
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import (
    FieldPanel,
    TabbedInterface,
    
)
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

# Create your models here.



class HeaderBanner(Page):
    template = "header/hearder.html"
    
    parent_page_type = [
        "home.HomePage",
    ]
    
    subpage_type = []
    
    banner_title  = models.CharField(max_length=20, blank=True, null=True)
    # banner_subtitle = StreamField(
    #     blocks.CharBlock(required=True)
    # )
    banner_subtitle = RichTextField()
    banner_image = ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    
    banner_cta = ForeignKey(
        "wagtailcore.Page",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    
    banner_panels = [
        MultiFieldPanel(
            [
                FieldPanel("banner_title"),
                FieldPanel("banner_subtitle"),
                ImageChooserPanel("banner_image"),
                PageChooserPanel("banner_cta"),
            ]
        )
    ]
    
    edit_handler = TabbedInterface(
        [
            ObjectList(banner_panels, heading="Banner"),
            ObjectList(Page.settings_panels, heading="Settings"),
            ObjectList(Page.promote_panels, heading ="Promote"),
        ]
    )
    
    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image"),
    ]
    
    
    
    class Meta:
        verbose_name = "Head"
        verbose_name_plural = "Headers"
        
    def get_admin_display_title(self):
        return "Header also for Banner"
    
