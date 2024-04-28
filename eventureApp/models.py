from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Users profile class


class UsersProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')
    city = models.CharField(max_length=50, blank=True, help_text='* City *')
    state = models.CharField(max_length=50, blank=True, help_text='* State *')
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
        return f"{self.user.username}'s profile"

# Create or save user profile

# Signal receiver to create a Profile whenever a User is created


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UsersProfile.objects.get_or_create(user=instance)

# Signal receiver to save the Profile whenever the User is saved


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()


# Events

class Event(models.Model):
    event_Name = models.CharField(max_length=200)
    event_location = models.CharField(max_length=200)
    event_date = models.DateTimeField()
    event_description = models.TextField()
    event_host_name = models.TextField()
    event_cost = models.TextField()
    event_number_of_attendees = models.IntegerField(
        default=0)  # Field for tracking the number of attendees
    event_external_url = models.URLField(
        max_length=200, blank=True)  # External events URL
    event_image = models.ImageField(
        upload_to='events_images/', null=True, blank=True)

    def __str__(self):
        return self.event_Name

    class Meta:
        app_label = 'eventureApp'
