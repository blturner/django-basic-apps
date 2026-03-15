from django.contrib import admin
from basic.media.models import *


@admin.action(description="Set selected photos content type to screenshot")
def make_screenshot(modeladmin, request, queryset):
    queryset.update(content_type=Photo.ContentType.SCREENSHOT)


class PhotoInline(admin.StackedInline):
    model = Photo


@admin.register(AudioSet)
class AudioSetAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(PhotoSet)
class PhotoSetAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('photos',)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'uploaded',
    ]
    prepopulated_fields = {'slug': ('title',)}
    actions = [make_screenshot]


@admin.register(Screenshot)
class ScreenshotAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded']


@admin.register(VideoSet)
class VideoSetAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
