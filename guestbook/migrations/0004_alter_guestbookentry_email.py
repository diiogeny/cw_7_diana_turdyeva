# Generated by Django 5.1.4 on 2024-12-07 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0003_guestbookentry_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestbookentry',
            name='email',
            field=models.EmailField(default='default@example.com', max_length=254),
        ),
    ]
