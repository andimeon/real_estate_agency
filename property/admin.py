from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'town_district', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'town', 'new_building', 'construction_year', 'price']
    list_editable = ['new_building']
    list_filter = ['new_building', 'has_balcony', 'active']
    

admin.site.register(Flat, FlatAdmin)
