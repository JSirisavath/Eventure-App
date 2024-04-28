from django.urls import path

from django.contrib import admin

# Views makes the html pages render to web app
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin
    path('', views.home, name='Welcome'),  # Home/Splash Page
    path('events-feed/', views.eventsFeed,
         name='Events Feed'),  # Events feed page
    path('signup/',  views.signup, name='Sign Up'),
    path('login/', views.login, name='Log In'),  # Log in page
    # Profile Page currently in progress
    path('profile/', views.view_own_users_profile, name='Profile'),
    path('editProfile/', views.update_profile,
         name='edit-profile'),  # Edit profile page
]
