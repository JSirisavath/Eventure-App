from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin



urlpatterns = [
    path('admin/', admin.site.urls),

    # Including all URL paths for Eventure App
    path('', include('eventureApp.urls')),

    # Authentication System
    # Also includes default auth urls
    path('accounts/', include('django.contrib.auth.urls'))
]
