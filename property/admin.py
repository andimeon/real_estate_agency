from django.contrib import admin

from .models import Flat, Claim


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'town_district', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'town', 'new_building', 'construction_year', 'price']
    list_editable = ['new_building']
    list_filter = ['new_building', 'has_balcony', 'active']
    raw_id_fields = ['liked_by']


class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ['rooms_number', 'user']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Claim, ClaimAdmin)