from django.contrib import admin

from .models import UsersProfile  # Users profile is accessible to admin console


admin.site.register(UsersProfile)
