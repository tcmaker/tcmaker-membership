from django.contrib import admin
from . import models
# Register your models here.

# admin.site.register(models.Membership)
admin.site.register(models.Discount)
admin.site.register(models.DuesPlan)
admin.site.register(models.Invitation)

@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'family_name', 'given_name', 'email', 'phone_number')
    fieldsets = (
        ('Basic Information', {
            'fields': ('given_name', 'family_name', 'email', 'member_since')
        }),

        ('Membership Information', {
            'fields': ('household', 'student_team')
        }),

        ('Address', {
            'fields': ('address_street1', 'address_street2', 'address_city', 'address_state', 'address_zip')
        }),

        ('Phone', {
            'fields': ('phone_number', 'phone_can_receive_sms')
        }),

        ('Emergency Contact Information', {
            'fields': ('emergency_contact_name', 'emergency_contact_phone')
        }),

        ('Staff Only', {
            'fields': ('notes',)
        })
    )

@admin.register(models.Household)
class HouseholdAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status', 'contact')

@admin.register(models.StudentTeam)
class StudentTeamAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status', 'contact')
