from django.contrib import admin
from basic.music.models import *


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display  = ('title', 'band',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
