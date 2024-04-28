from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UsersProfile

# Sign up form will use user's profile class setup


class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True)
    user_name = forms.CharField(max_length=50, required=True)
    city = forms.CharField(max_length=50, required=True)
    state = forms.CharField(max_length=50, required=True)
    instagram_username = forms.CharField(max_length=30, required=False)
    facebook_username = forms.CharField(max_length=30, required=False)
    linkedin_username = forms.CharField(max_length=30, required=False)
    interests = forms.CharField(widget=forms.Textarea, required=False)
    events_attended = forms.IntegerField(
        required=False, initial=0, help_text='Enter how many events you have attended.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'full_name', 'city', 'state',
                  'instagram_username', 'facebook_username', 'linkedin_username', 'interests', 'events_attended')

    # Save users
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.profile.full_name = self.cleaned_data.get('full_name', '')
            user.profile.city = self.cleaned_data.get('city', '')
            user.profile.state = self.cleaned_data.get('state', '')
            user.profile.instagram_username = self.cleaned_data.get(
                'instagram_username', '')
            user.profile.facebook_username = self.cleaned_data.get(
                'facebook_username', '')
            user.profile.linkedin_username = self.cleaned_data.get(
                'linkedin_username', '')
            user.profile.interests = self.cleaned_data.get('interests', '')
            user.profile.events_attended = self.cleaned_data.get(
                'events_attended', 0)  # Save this new field
            user.profile.save()
        return user
