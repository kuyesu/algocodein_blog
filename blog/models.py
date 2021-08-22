from django.db import models

# Create your models here.
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, TranslatableMixin
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, PageChooserPanel, InlinePanel

from django_comments_xtd.models import XtdComment


from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField
from modelcluster.fields import ParentalManyToManyField, ParentalKey
from modelcluster.models import ClusterableModel

class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.CharBlock(required=False)

    class Meta:
        icon = 'image'


class StoryBlock(blocks.StreamBlock):
    heading = blocks.CharBlock()
    paragraph = blocks.RichTextBlock()
    image = ImageBlock()


@register_snippet
class BlogCategory(TranslatableMixin):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class BlogPostPage(Page):
    publication_date = models.DateField(null=True, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True
    )
    body = StreamField(StoryBlock())
    category = models.ForeignKey(
        BlogCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='blog_posts'
    )

    content_panels = Page.content_panels + [
        FieldPanel('publication_date'),
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
        SnippetChooserPanel('category'),
        InlinePanel('customcomments', label=_("Comments")),
    ]

    parent_page_types = ['blog.BlogIndexPage']

    def get_absolute_url(self):
        return self.get_url()



class BlogIndexPage(Page):
    introduction = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduction'),
    ]

    parent_page_types = ['home.HomePage']


class CustomComment(XtdComment):
    page = ParentalKey(BlogPostPage, on_delete=models.CASCADE, related_name='customcomments')

    def save(self, *args, **kwargs):
        if self.user:
            self.user_name = self.user.display_name
        self.page = BlogPostPage.objects.get(pk=self.object_pk)
        super(CustomComment, self).save(*args, **kwargs)