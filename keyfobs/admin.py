from django.contrib import admin
from .models import Keyfob, AccessOverride

class KeyfobAdmin(admin.ModelAdmin):
    search_fields = ['person__family_name', 'person__given_name']
    ordering = ('person__family_name', 'person__given_name')

admin.site.register(Keyfob, KeyfobAdmin)

class AccessOverrideAdmin(admin.ModelAdmin):
    list_display = ['description', 'person', 'start_at', 'end_at']
    search_fields = ['person__family_name', 'person__given_name', 'description']
    ordering = ['description',]

admin.site.register(AccessOverride, AccessOverrideAdmin)
