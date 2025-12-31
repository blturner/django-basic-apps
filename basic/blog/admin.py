from django.contrib import admin
from basic.blog.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display  = ('title', 'publish', 'status')
    list_filter   = ('sites', 'publish', 'categories', 'status')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}


class BlogRollAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'sort_order',)
    list_editable = ('sort_order',)
admin.site.register(BlogRoll)