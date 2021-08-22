from django.contrib import admin

# Register your models here.
from .models import MenuItem, Menu
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline



class MenuItemInline(TranslationTabularInline):
    model = MenuItem


class MenuAdmin(TranslationAdmin):
    model = Menu
    inlines = [MenuItemInline,]


admin.site.register(Menu, MenuAdmin)
