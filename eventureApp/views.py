from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

# For splash page


def home(request):
    return render(request, 'home.html')


# Events Feed page- Only accessible to users that have a login
# Will show users curated events to join/RSVP
# Events should also events cards to view and choose from
# @login_required
def eventsFeed(request):
    return render(request, 'eventsFeed.html')

# # For sign_up.html


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the login page after sign up *** Need to change to events page
            return redirect(reverse('login'))
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


# Login *** Need to add more login information logic
def login(request):
    return redirect(request, 'login.html')
