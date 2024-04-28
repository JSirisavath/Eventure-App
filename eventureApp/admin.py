from django.contrib import admin

from .models import UsersProfile  # Users profile is accessible to admin console

# Register your models here.
admin.site.register(UsersProfile)
