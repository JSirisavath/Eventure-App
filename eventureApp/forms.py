from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsersProfile
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
