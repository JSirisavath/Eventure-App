from django.contrib import admin

# Users profile and Events is accessible to admin console
from .models import UsersProfile, Event


admin.site.register(UsersProfile)


class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_location',
                    'event_date', 'event_host_name', 'event_cost')
    # If you're using fieldsets or any other field-specific options, ensure they also match:
    fieldsets = (
        (None, {
            'fields': ('event_name', 'event_location', 'event_date', 'event_description', 'event_image')
        }),)


# Register events to admin
admin.site.register(Event)
