from django.db import models
from django.db.models.fields.related import ForeignKey

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    StreamFieldPanel,
    PageChooserPanel,
    ObjectList,
    TabbedInterface,
)
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks


class HomePage(Page):
    """The home page models"""
    template = "home/home_page.html"
    # max_count = 1
    subpage_types = [
        # 'blog.BlogListingPage',
        'contact.ContactPage',
        'about.AboutUs',
    ]
    parent_page_type = [
        'wagtailcore.Page'
    ]

    banner_title = models.CharField(max_length=45, null=True, blank=False)
    banner_subtitle = RichTextField(features=["bold", "italic", "link"],null=True, blank=False)
    banner_image = ForeignKey(
        "wagtailimages.Image",
        blank=False,
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
    
    
    events = StreamField(
        [
            ("events", blocks.UpConingEvents()),
            ("cta", blocks.CTABlock(required=False)),
            ("richtext", blocks.RichtextBlock()),
            ("simpletext", blocks.SimpleRichtextBlock()),
            ("cta", blocks.CTABlock()),
            # ("buttonlogic", blocks.LinkStructValue()),
            ("cardBlock", blocks.CardBlock()),
            ("titleandtext", blocks.TitleAndTextBlock())
        ],
        null=True,
        blank=True,
        
    )
    
    
    activities = StreamField(
        [
            ("activities", blocks.Activities()),
            ("richtext", blocks.RichtextBlock()),
            ("simpletext", blocks.SimpleRichtextBlock()),
            ("cta", blocks.CTABlock()),
            # ("buttonlogic", blocks.LinkStructValue()),
            ("cardBlock", blocks.CardBlock()),
            ("titleandtext", blocks.TitleAndTextBlock())
        ],
        null=True,
        blank=True,
        # min_num=1, 
        max_num=4
    )
    
    
    """This is foe sliding images"""
    
    
    Sliding_Images_Content = StreamField(
        [
            ("sliding_images", blocks.SlidingImage()),
            ("cta", blocks.CTABlock(required=False)),
            ("richtext", blocks.RichtextBlock()),
            ("simpletext", blocks.SimpleRichtextBlock()),
            ("cta", blocks.CTABlock()),
            # ("buttonlogic", blocks.LinkStructValue()),
            ("cardBlock", blocks.CardBlock()),
            ("titleandtext", blocks.TitleAndTextBlock())
            
        ],
        null=True,
        blank=True,
        
    )
    
    
    
    """Jumbo_Banner """
    Jumbo_Banner = StreamField(
        [
            ("JumboBanner", blocks.JumboBanner()),
            ("cta", blocks.CTABlock(required=False)),
            ("richtext", blocks.RichtextBlock()),
            ("simpletext", blocks.SimpleRichtextBlock()),
            ("cta", blocks.CTABlock()),
            # ("buttonlogic", blocks.LinkStructValue()),
            ("cardBlock", blocks.CardBlock()),
            ("titleandtext", blocks.TitleAndTextBlock())
        ],
        null=True,
        blank=True,
    )
    
    
    
    
    """MoreGenericMessage"""
    card_Message = StreamField(
        [
            ("CardMessage", blocks.CardMessage()),
            ("cta", blocks.CTABlock(required=False)),
            ("cardBlock", blocks.CardBlock()),
            ("titleandtext", blocks.TitleAndTextBlock()),
            ("richtext", blocks.RichtextBlock()),
            ("simpletext", blocks.SimpleRichtextBlock()),
            ("cta", blocks.CTABlock()),
        ],
        null=True,
        blank=True,
    )
    
    
    
    
    
    
    
    """ALL PANELS HERE"""
    """"banner panels"""
    
    banner_panels = [
        MultiFieldPanel(
            [
                FieldPanel("banner_title"),
                FieldPanel("banner_subtitle"),
                ImageChooserPanel("banner_image"),
                PageChooserPanel("banner_cta"),
            ],
                heading="Banner Options",
        ),
    ]
    
    """popular_content panel"""
    events_panel = [
        StreamFieldPanel("events"),
          
    ]
    
    """panels for section part3 """
    activities_panels = [
        MultiFieldPanel(
            [
                StreamFieldPanel("activities"),
            ],
            heading = "Activities",
        ),
    ]
    
    """Sliding_Images"""
    Sliding_Images_panel = [
        StreamFieldPanel("Sliding_Images_Content"),
    ]
    
    Jumbo_Banner_panel=[
        StreamFieldPanel("Jumbo_Banner"),
    ]
    
    card_Message_panel = [
        StreamFieldPanel("card_Message"),
    ]
#     edit_handler = TabbedInterface(
#         [
#             ObjectList(content_panels, heading='Content'),
#             ObjectList(banner_panels, heading="Banner Settings"),
#             ObjectList(Page.promote_panels, heading='Promotional Stuff'),
#             ObjectList(Page.settings_panels, heading='Settings Stuff'),
#         ]
#   )
    
    edit_handler = TabbedInterface(
        [
            ObjectList(banner_panels, heading="Banner Settings"),
            ObjectList(events_panel, heading = "Events"),
            ObjectList(activities_panels, heading = "Activities"),
            ObjectList(Sliding_Images_panel, heading = "Sliding Images"),
            ObjectList(Jumbo_Banner_panel, heading = "Jumbo"),
            ObjectList(card_Message_panel, heading="Message Card"),
            ObjectList(Page.settings_panels, heading="Setting"),
            ObjectList(Page.promote_panels, heading='Promotional'),
        ]
    )
    
    
    
    class Meta:
        verbose_name = "Home Page"
        verbose_name = "Home Pages"
        
        
    def get_admin_display_title(self):
        return "Home Page"