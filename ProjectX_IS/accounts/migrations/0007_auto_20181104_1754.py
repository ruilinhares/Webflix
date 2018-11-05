# Generated by Django 2.1.2 on 2018-11-04 17:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20181102_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('phone_number', models.IntegerField(blank=True)),
                ('card_number', models.CharField(blank=True, max_length=15)),
                ('card_validity', models.DateField(blank=True)),
                ('date_joined', models.DateTimeField(default=datetime.datetime(2018, 11, 4, 17, 54, 55, 536424, tzinfo=utc), verbose_name='date_joined')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Episode',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='movie_list',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('ACTION', 'Action'), ('ADVENTURE', 'Adventure'), ('COMEDY', 'Comedy'), ('DRAMA', 'Drama'), ('FANTASY', 'Fantasy'), ('HISTORY', 'History'), ('MYSTERY', 'Mystery'), ('ROMANCE', 'Romance'), ('SCIENCE FICTION', 'Science fiction)'), ('THRILLER', 'Thriller')], default='', max_length=20),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.AddField(
            model_name='customuser',
            name='movie_list',
            field=models.ManyToManyField(to='accounts.Movie'),
        ),
    ]