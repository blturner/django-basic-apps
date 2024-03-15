from django.contrib import admin
from basic.places.models import *


@admin.register(PlaceType)
class PlaceTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('city', 'state')}


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ('address', 'city', 'zip', 'latitude', 'longitude')
    list_filter = ('city',)
    search_fields = ('address',)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'point', 'city', 'status')
    list_filter = ('status', 'place_types')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
