from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Movie(models.Model):
    image = models.FileField(upload_to='static/', default='')
    title = models.CharField(max_length=50, default='')
    director = models.CharField(max_length=50, default='')
    year = models.IntegerField(default=1900)
    CATEGORY_CHOICE = (
        ('ACTION', 'Action'),
        ('ADVENTURE', 'Adventure'),
        ('COMEDY', 'Comedy'),
        ('DRAMA', 'Drama'),
        ('FANTASY', 'Fantasy'),
        ('HISTORY', 'History'),
        ('MYSTERY', 'Mystery'),
        ('ROMANCE', 'Romance'),
        ('SCIENCE FICTION', 'Science fiction'),
        ('THRILLER', 'Thriller')
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICE, default='')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

    phone_number = models.IntegerField(blank=True, default='0')
    card_number = models.CharField(max_length=15, blank=True)
    movie_list = models.ManyToManyField(Movie)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


