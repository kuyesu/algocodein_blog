from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, PageChooserPanel, InlinePanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet


# Create your models here.
@register_snippet
class Privacy(models.Model):
    name = models.CharField(max_length=250)
    statement = RichTextField(blank=True)

    panels = [
        FieldPanel('name', classname='full'),
        FieldPanel('statement', classname='full'),
    ]

    def __str__(self):
        return self.name

    class Meta:
    	verbose_name = "Privacy Policy"
    	verbose_name_plural = "Privacy Policies"

# Create your models here.
@register_snippet
class Cookies(models.Model):
    name = models.CharField(max_length=250)
    statement = RichTextField(blank=True)

    panels = [
        FieldPanel('name', classname='full'),
        FieldPanel('statement', classname='full'),
    ]

    def __str__(self):
        return self.name


    class Meta:
    	verbose_name = "Cookies"
    	verbose_name_plural = "Cookies"
