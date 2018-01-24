# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Category, Location, Image

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('Category',)

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Image)