# Generated by Django 2.1.1 on 2018-09-15 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_ip_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='ip_user',
        ),
    ]