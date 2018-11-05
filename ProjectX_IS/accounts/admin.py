from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

from .models import Profile, Movie

admin.site.register(Profile)
admin.site.register(Movie)
