# Generated by Django 3.1.7 on 2021-04-17 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_userlastactivity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserActivity',
        ),
    ]