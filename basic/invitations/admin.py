from django.contrib import admin

from basic.invitations.models import Invitation, InvitationAllotment


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'email', 'name', 'status', 'created')
    list_filter = ('status',)
    raw_id_fields = ('from_user',)


@admin.register(InvitationAllotment)
class InvitationAllotmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount')
    raw_id_fields = ('user',)
