# Generated by Django 4.2.7 on 2024-04-28 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventureApp', '0002_remove_usersprofile_full_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersprofile',
            name='user',
            field=models.OneToOneField(help_text='Create your username!', on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
