from django.contrib import admin
from basic.bookmarks.models import *


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('url', 'description')
    search_fields = ('url', 'description', 'extended')
    prepopulated_fields = {'slug': ('title',)}
