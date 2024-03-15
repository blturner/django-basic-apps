from django.contrib import admin
from basic.flagging.models import *


@admin.register(FlagType)
class FlagTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Flag)
class FlagAdmin(admin.ModelAdmin):
    list_display = ('object', 'flag_type')
    list_filter = ('flag_type',)
    raw_id_fields = ('user',)
