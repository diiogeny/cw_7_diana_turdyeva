# Generated by Django 5.1.4 on 2024-12-07 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0002_remove_guestbookentry_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestbookentry',
            name='email',
            field=models.EmailField(default='Email', max_length=254),
        ),
    ]
