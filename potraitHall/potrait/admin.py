# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Category, Location, Image

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('categories',)

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Image,ImageAdmin )