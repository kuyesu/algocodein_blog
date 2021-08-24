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
    
    works = StreamField(
        [
            ("works", blocks.Works()),
            ("events", blocks.UpConingEvents()),
            ("activities", blocks.Activities()),
            ("JumboBanner", blocks.JumboBanner()),
            ("smallbanner", blocks.SmallBanner()),
            ("Testimonies", blocks.Testimonies()),
            ("partners", blocks.Partners()),
            ("CardMessage", blocks.CardMessage()),
            ("technologies", blocks.Technologies()),
            ("CardLight", blocks.CardLight()),
            ("CardImage", blocks.CardImage()),
            ("CardGeneric", blocks.CardGeneric()),
            ("cta", blocks.CTABlock(required=False)),
            # ("cta", blocks.CTABlock(required=False)),
            ("richtext", blocks.RichtextBlock()),
            ("simpletext", blocks.SimpleRichtextBlock()),
            # ("cta", blocks.CTABlock()),
            # ("buttonlogic", blocks.LinkStructValue()),
            ("cardBlock", blocks.CardBlock()),
            ("button", blocks.ButtonBlock()),
            ("titleandtext", blocks.TitleAndTextBlock()),
            ("sliding_images", blocks.SlidingImage()),
        ],
        null=True,
        blank=True,
        
    )
    
    
    events = StreamField(
        [
            
            ("events", blocks.UpConingEvents()),
            ("activities", blocks.Activities()),
            ("works", blocks.Works()),
            ("JumboBanner", blocks.JumboBanner()),
            ("Testimonies", blocks.Testimonies()),
            ("partners", blocks.Partners()),
            ("smallbanner", blocks.SmallBanner()),
            ("CardMessage", blocks.CardMessage()),
            ("technologies", blocks.Technologies()),
            ("CardLight", blocks.CardLight()),
            ("CardImage", blocks.CardImage()),
            ("CardGeneric", blocks.CardGeneric()),
            ("cta", blocks.CTABlock(required=False)),
            # ("cta", blocks.CTABlock(required=False)),
            ("richtext", blocks.RichtextBlock()),
            ("simpletext", blocks.SimpleRichtextBlock()),
            # ("cta", blocks.CTABlock()),
            # ("buttonlogic", blocks.LinkStructValue()),
            ("cardBlock", blocks.CardBlock()),
            ("button", blocks.ButtonBlock()),
            ("titleandtext", blocks.TitleAndTextBlock()),
            ("sliding_images", blocks.SlidingImage()),
        ],
        null=True,
        blank=True,
        
    )
    
    
    activities = StreamField(
        [
            ("activities", blocks.Activities()),
            ("works", blocks.Works()),
            ("events", blocks.UpConingEvents()),
            ("richtext", blocks.RichtextBlock()),
            ("simpletext", blocks.SimpleRichtextBlock()),
            ("JumboBanner", blocks.JumboBanner()),
            ("Testimonies", blocks.Testimonies()),
            ("partners", blocks.Partners()),
            ("smallbanner", blocks.SmallBanner()),
            ("CardMessage", blocks.CardMessage()),
            ("technologies", blocks.Technologies()),
            ("CardLight", blocks.CardLight()),
            ("CardImage", blocks.CardImage()),
            ("CardGeneric", blocks.CardGeneric()),
            ("cta", blocks.CTABlock(required=False)),
            # ("cta", blocks.CTABlock()),
            # ("buttonlogic", blocks.LinkStructValue()),
            ("cardBlock", blocks.CardBlock()),
            ("titleandtext", blocks.TitleAndTextBlock()),
            ("button", blocks.ButtonBlock()),
            ("sliding_images", blocks.SlidingImage()),
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
            ("activities", blocks.Activities()),
            ("works", blocks.Works()),
            ("events", blocks.UpConingEvents()),
            ("JumboBanner", blocks.JumboBanner()),
            ("Testimonies", blocks.Testimonies()),
            ("partners", blocks.Partners()),
            ("smallbanner", blocks.SmallBanner()),
            ("CardMessage", blocks.CardMessage()),
            ("technologies", blocks.Technologies()),
            ("CardLight", blocks.CardLight()),
            ("CardImage", blocks.CardImage()),
            ("CardGeneric", blocks.CardGeneric()),
            # ("cta", blocks.CTABlock(required=False)),
            ("cta", blocks.CTABlock(required=False)),
            ("richtext", blocks.RichtextBlock()),
            ("simpletext", blocks.SimpleRichtextBlock()),
            # ("cta", blocks.CTABlock()),
            # ("buttonlogic", blocks.LinkStructValue()),
            ("cardBlock", blocks.CardBlock()),
            ("titleandtext", blocks.TitleAndTextBlock()),
            ("button", blocks.ButtonBlock()),
            
        ],
        null=True,
        blank=True,
        
    )
    
    
    
    """Jumbo_Banner """
    Jumbo_Banner = StreamField(
        [
            ("JumboBanner", blocks.JumboBanner()),
            ("smallbanner", blocks.SmallBanner()),
            ("sliding_images", blocks.SlidingImage()),
            ("activities", blocks.Activities()),
            ("works", blocks.Works()),
            ("events", blocks.UpConingEvents()),
            ("Testimonies", blocks.Testimonies()),
            ("partners", blocks.Partners()),
            ("CardMessage", blocks.CardMessage()),
            ("technologies", blocks.Technologies()),
            ("CardLight", blocks.CardLight()),
            ("CardImage", blocks.CardImage()),
            ("CardGeneric", blocks.CardGeneric()),
            ("cta", blocks.CTABlock(required=False)),
            ("richtext", blocks.RichtextBlock()),
            ("simpletext", blocks.SimpleRichtextBlock()),
            # ("cta", blocks.CTABlock()),
            # ("buttonlogic", blocks.LinkStructValue()),
            ("cardBlock", blocks.CardBlock()),
            ("titleandtext", blocks.TitleAndTextBlock()),
            ("button", blocks.ButtonBlock()),
        ],
        null=True,
        blank=True,
    )
    
    
    
    
    """MoreGenericMessage"""
    cards = StreamField(
        [
            ("CardMessage", blocks.CardMessage()),
            ("technologies", blocks.Technologies()),
            ("CardLight", blocks.CardLight()),
            ("CardImage", blocks.CardImage()),
            ("CardGeneric", blocks.CardGeneric()),
            ("JumboBanner", blocks.JumboBanner()),
            ("Testimonies", blocks.Testimonies()),
            ("partners", blocks.Partners()),
            ("smallbanner", blocks.SmallBanner()),
            ("sliding_images", blocks.SlidingImage()),
            ("activities", blocks.Activities()),
            ("works", blocks.Works()),
            ("events", blocks.UpConingEvents()),
            ("button", blocks.ButtonBlock()),
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
    
    works_panel = [
        StreamFieldPanel("works"),
          
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
    
    card_panel = [
        StreamFieldPanel("cards"),
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
            ObjectList(works_panel, heading = "Works"),
            ObjectList(activities_panels, heading = "Activities"),
            ObjectList(Sliding_Images_panel, heading = "Sliding Images"),
            ObjectList(Jumbo_Banner_panel, heading = "Jumbo"),
            ObjectList(card_panel, heading="All Card"),
            ObjectList(Page.settings_panels, heading="Setting"),
            ObjectList(Page.promote_panels, heading='Promotional'),
        ]
    )
    
    
    
    class Meta:
        verbose_name = "Home Page"
        verbose_name = "Home Pages"
        
        
    def get_admin_display_title(self):
        return "Home Page"