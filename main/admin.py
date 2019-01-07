# -*- coding: utf-8 -*-

from django.contrib import admin
from main.models import *

# Register your models here.

class PoiAdmin(admin.ModelAdmin):
	list_display = ('pk', 'title', 'city', 'country', 'poi_type', 'lat', 'lng', )
	list_filter = ('poi_type', 'country', )
	search_fields = ('title', 'lat', 'lng', )


admin.site.register(Poi, PoiAdmin)