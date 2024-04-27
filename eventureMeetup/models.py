from django.db import models

# Create your models here.

# Users profile


class userProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    bio = models.TextField()

    def __str__(self):
        return self.user.username

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

    def __str__(self):
        return self.event_Name
