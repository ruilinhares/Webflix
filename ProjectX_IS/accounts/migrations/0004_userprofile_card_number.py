# Generated by Django 2.1.2 on 2018-11-02 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_delete_creditcard'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='card_number',
            field=models.CharField(default='', max_length=15),
        ),
    ]