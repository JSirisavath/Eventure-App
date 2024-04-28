from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsersProfile, Event
from django.contrib.auth import get_user_model

# Sign up form will use user's profile class setup


class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    # Save users

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            UsersProfile.objects.create(user=user)
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UsersProfile
        fields = '__all__'
        widgets = {
            'interests': forms.Textarea(attrs={'rows': 4}),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_Name', 'event_date',
                  'event_location', 'event_host_name', 'event_number_of_attendees',
                  'event_cost', 'event_description', 'event_external_url']
