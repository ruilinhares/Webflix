from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from apscheduler.schedulers.background import BackgroundScheduler as Scheduler
from django.core.mail import send_mail

from datetime import datetime, timedelta

# Start the scheduler
sched = Scheduler()
sched.start()


# Define the function that is to be executed
def my_job():
    print("payment verification...")
    users = User.objects.all()
    today = datetime.today()

    emails = list()
    for user in users:
        if user.date_joined.day == today.day and user.date_joined.month != today.month:
            user.date_joined = today
            user.save()
            emails.append(user.username)
    print(emails)
    if emails:
        send_mail('Webflix payment',
                  'Your payment has been processed successfully.\n\nBest regards,\nWeblifx',
                  'email@gmail.com',
                  emails)
    run_day = today + timedelta(days=1)
    print(run_day)
    sched.add_job(my_job, next_run_time=run_day)


today = datetime.today() + timedelta(0, 60)
print(today)
sched.add_job(my_job, next_run_time=today)


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
