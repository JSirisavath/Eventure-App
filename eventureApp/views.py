from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .models import UsersProfile

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
            user = form.save()
            profile = UsersProfile.objects.get_or_create(user=user)[0]
            profile.full_name = form.cleaned_data.get('full_name')
            profile.city = form.cleaned_data.get('city')
            profile.save()
            # login users
            login(request, user)

            # Redirect to users profile
            return redirect('UsersProfile')
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
