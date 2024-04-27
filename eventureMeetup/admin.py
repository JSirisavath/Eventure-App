from django.contrib import admin

from .models import userProfile  # Users profile is accessible to admin console

# Events import
from .models import Event

# Register app to admin
admin.site.register(userProfile)


# Register Events to admin console

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_Name', 'event_location',
                    'event_date', 'event_description', 'event_host_name', 'event_cost', 'event_number_of_attendees', 'event_external_url')

    fields = ['event_Name', 'event_date', 'event_location',
              'event_description',
              'event_host_name',
              'event_number_of_attendees', 'event_external_url', 'event_cost']


admin.site.register(Event, EventAdmin)
