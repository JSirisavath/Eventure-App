
from django.urls import path
from .views import home
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    # path('dashboard/', dashboard, name='dashboard'),
    # path('events-feed/', events_feed, name='events_feed'),
    # path('sign-up/', sign_up, name='sign_up'),
]
