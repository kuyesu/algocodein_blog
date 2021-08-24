from wagtail.core import blocks
from wagtail.core.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    """Title and text and nothing else."""

    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add additional text")

    class Meta:  # noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class CardBlock(blocks.StructBlock):
    """Cards with image and text and button(s)."""

    title = blocks.CharBlock(required=True, help_text="Add your title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )

    class Meta:  # noqa
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Staff Cards"

class Works(blocks.StructBlock):
   
    Herbs_Facts_cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=25)),
                ("text", blocks.TextBlock(required=True, max_length=80)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta:  # noqa
        template = "streams/home_facts.html"
        icon = "placeholder"
        label = "Works"


"""Home page Section Popular herbs"""
class UpConingEvents(blocks.StructBlock):
   
    Herbs_Facts_cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=25)),
                ("text", blocks.TextBlock(required=True, max_length=80)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta:  # noqa
        template = "streams/home_facts.html"
        icon = "placeholder"
        label = "Events"





class Activities(blocks.StructBlock):
   
    Popular_herbs_cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta:  # noqa
        template = "streams/home_popular_herbs.html"
        icon = "placeholder"
        label = "Activitie"





class SlidingImage(blocks.StructBlock):
    """These are for sliding images"""
    Sliding_Images = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )

    class Meta: #noqa
        template = "streams/sliding_images.html"
        icon = "image"
        label = "Sliding Image"



       
class JumboBanner(blocks.StructBlock):
    """Jumbo banner for the bottom"""
    JumboBanner_Card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True)),
                ("subtitle",blocks.TextBlock(required=True, max_length=200)),
                ("image", ImageChooserBlock(required=False)),
                ("Link_to_a_page", blocks.CharBlock(required=True)),
                ("Link_to_external_page", blocks.CharBlock(required=False)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )


    class Meta: #noqa
        template = "streams/jumbobanner_page.html"
        icon = "image"
        label = "Large Banner"

class SmallBanner(blocks.StructBlock):
    """Jumbo banner for the bottom"""
    JumboBanner_Card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True)),
                ("subtitle",blocks.TextBlock(required=True, max_length=200)),
                ("image", ImageChooserBlock(required=False)),
                ("Link_to_a_page", blocks.CharBlock(required=False)),
                ("Link_to_external_page", blocks.CharBlock(required=False)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )


    class Meta: #noqa
        template = "streams/small_banner.html"
        icon = "image"
        label = "Small Banner"



class CardMessage(blocks.StructBlock):

    message_Card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("image", ImageChooserBlock(required=True)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/moregenericmessage_page.html"
        icon = "edit"
        label = "Message Card"
        
class CardLight(blocks.StructBlock):

    message_Card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("image", ImageChooserBlock(required=True)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/moregenericmessage_page.html"
        icon = "edit"
        label = "Light Card"

class CardImage(blocks.StructBlock):

    message_Card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("image", ImageChooserBlock(required=True)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/moregenericmessage_page.html"
        icon = "image"
        label = "Image Card"


class CardGeneric(blocks.StructBlock):

    message_Card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("image", ImageChooserBlock(required=True)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/moregenericmessage_page.html"
        icon = "doc-full"
        label = "Generic Card" 
        
class Technologies(blocks.StructBlock):

    message_Card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=False, max_length=200)),
                ("image", ImageChooserBlock(required=True)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/technology.html"
        icon = "phone"
        label = "Technology"
        
class Testimonies(blocks.StructBlock):

    message_Card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("subtitle", blocks.CharBlock(required=True, max_length=40)),
                
                ("image", ImageChooserBlock(required=True)),
                ("Name", blocks.CharBlock(required=True, max_length=40)),
                ("job_title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=False, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/testimonies.html"
        icon = "phone"
        label = "Testimonies"  
        
class Partners(blocks.StructBlock):

    message_Card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("subtitle", blocks.CharBlock(required=True, max_length=40)),
                ("image", ImageChooserBlock(required=True)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/partners.html"
        icon = "phone"
        label = "Partners"  
# ------------------------------------------------------------------------




class RichtextBlock(blocks.RichTextBlock):
    """Richtext with all the features."""

    def get_api_representation(self, value, context=None):
        return richtext(value.source)

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"


class SimpleRichtextBlock(blocks.RichTextBlock):
    """Richtext without (limited) all the features."""

    def __init__(
        self, required=True, help_text=None, editor="default", features=None, **kwargs
    ):  # noqa
        super().__init__(**kwargs)
        self.features = ["bold", "italic", "link"]

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Simple RichText"


class CTABlock(blocks.StructBlock):
    """A simple call to action section."""

    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.RichTextBlock(required=True, features=["bold", "italic"])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default='Learn More', max_length=40)
    

    class Meta:  # noqa
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "Call to Action"


class LinkStructValue(blocks.StructValue):
    """Additional logic for our urls."""

    def url(self):
        button_page = self.get('button_page')
        button_url = self.get('button_url')
        if button_page:
            return button_page.url
        elif button_url:
            return button_url

        return None

    # def latest_posts(self):
    #     return BlogDetailPage.objects.live()[:3]


class ButtonBlock(blocks.StructBlock):
    """An external or internal URL."""
    button_title = blocks.CharBlock(required=True)
    button_page = blocks.PageChooserBlock(required=False, help_text='If selected, this url will be used first')
    button_url = blocks.URLBlock(required=False, help_text='If added, this url will be used secondarily to the button page')

    # def get_context(self, request, *args, **kwargs):
    #     context = super().get_context(request, *args, **kwargs)
    #     context['latest_posts'] = BlogDetailPage.objects.live().public()[:3]
    #     return context

    class Meta:  # noqa
        template = "streams/button_block.html"
        icon = "link"
        label = "Button"
value_class = LinkStructValue