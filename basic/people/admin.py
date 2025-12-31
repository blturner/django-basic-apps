from django.contrib import admin
from basic.people.models import *


@admin.register(PersonType)
class PersonTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_filter = ('person_types',)
    search_fields = ('first_name', 'last_name')
    prepopulated_fields = {'slug': ('first_name','last_name')}


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('person','quote')
    list_filter = ('person',)
    search_fields = ('quote',)


class ConversationItemInline(admin.StackedInline):
    model = ConversationItem
    fk = 'conversation'


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    inlines = [
        ConversationItemInline
    ]
admin.site.register(ConversationItem)