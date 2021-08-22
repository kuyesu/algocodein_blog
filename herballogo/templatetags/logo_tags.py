from herballogo.models import  CompanyLogo
from django import template
from django.utils import translation

register = template.Library()


@register.simple_tag()
def company_logo():
    return CompanyLogo.objects.first()
