# For base.html
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

# For dashboard.html
def dashboard(request):
    return render(request, 'dashboard.html')

# For events_feed.html
def events_feed(request):
    return render(request, 'events_feed.html')

# For sign_up.html
def sign_up(request):
    return render(request, 'sign_up.html')

