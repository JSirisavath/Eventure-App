from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Users profile class


class UsersProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, help_text='Create your username!')
    full_name = models.CharField(
        max_length=100, blank=False, help_text='* Full Name *')
    city = models.CharField(max_length=50, blank=False, help_text='* City *')
    state = models.CharField(max_length=50, blank=False, help_text='* State *')
    users_email = models.EmailField(max_length=254, help_text='Email address')
    instagram_username = models.CharField(
        max_length=30, blank=True, help_text='Instagram')
    facebook_username = models.CharField(
        max_length=30, blank=True, help_text='FaceBook')
    linkedin_username = models.CharField(
        max_length=30, blank=True, help_text='LinkedIn')

    interests = models.TextField(
        blank=True, help_text='Let us know about your interests!')
    events_attended = models.IntegerField(default=0)

    class Meta:
        app_label = 'eventureApp'

    def __str__(self):
        return self.user.username

# Create or update user profile


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UsersProfile.objects.create(user=instance)
    instance.profile.save()
