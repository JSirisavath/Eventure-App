from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import SignUpForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import UsersProfile, Event
from django.contrib.auth import login as auth_login

from django.contrib.auth import authenticate
import logging


logger = logging.getLogger(__name__)
# For splash page


def home(request):
    return render(request, 'home.html')


# Events Feed page- Only accessible to users that have a login
# Will show users curated events to join/RSVP
# Events should also events cards to view and choose from
# @login_required
def eventsFeed(request):
    events = Event.objects.all().order_by('event_date')
    return render(request, 'eventsFeed.html', {'events': events})

# # For sign_up.html


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            # Authenticate the user
            user = authenticate(username=user.username,
                                password=form.cleaned_data['password1'])
            if user is not None:
                auth_login(request, user)  # Log the user in
                return redirect('EventsFeed')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
# Login *** Need to add more login information logic


def login(request):
    return redirect(request, 'login.html')


def view_own_users_profile(request):
    # Get Profile link to logged in user
    profile = UsersProfile.objects.get(user=request.user)
    return render(request, 'UsersProfile.html', {'profile': profile})


# Update profile
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('UsersProfile')

    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'editProfile.html', {'form': form})



def intersts_page(request):
    return render(request, 'InterestsPage.html')