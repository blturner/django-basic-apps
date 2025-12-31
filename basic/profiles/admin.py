from django.contrib import admin
from basic.profiles.models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('profile', 'service')
    list_filter = ('profile', 'service')


admin.site.register(MobileProvider)
admin.site.register(ServiceType)
admin.site.register(Link)