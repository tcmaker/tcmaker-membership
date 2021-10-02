from django.contrib import admin
from .models import Keyfob

class KeyfobAdmin(admin.ModelAdmin):
    search_fields = ['person__family_name', 'person__given_name']
    # autocomplete_fields = ['person__family_name', 'person__given_name']
    ordering = ('person__family_name', 'person__given_name')

admin.site.register(Keyfob, KeyfobAdmin)
