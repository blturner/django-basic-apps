from django.contrib import admin
from basic.books.models import *


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display  = ('title', 'pages')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Highlight)
class HighlightAdmin(admin.ModelAdmin):
    list_display  = ('book', 'highlight')
    list_filter   = ('book',)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('book', 'current_page')
