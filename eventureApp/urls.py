from django.urls import path

# Views makes the html pages render to web app
from . import views

urlpatterns = [
    path('', views.home, name='Welcome'),  # Home/Splash Page
    path('events-feed/', views.eventsFeed,
         name='Events Feed'),  # Events feed page
    path('signup/',  views.signup, name='Sign Up'),
    path('login/', views.login, name='Log In')  # Log in page
]
