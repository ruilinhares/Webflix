# Generated by Django 2.1.2 on 2018-11-02 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20181102_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='card_validity',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='movie_list',
            field=models.ManyToManyField(to='accounts.Movie'),
        ),
    ]
