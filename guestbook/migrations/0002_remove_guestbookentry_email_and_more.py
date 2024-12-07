# Generated by Django 5.1.4 on 2024-12-07 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guestbookentry',
            name='email',
        ),
        migrations.AddField(
            model_name='guestbookentry',
            name='author_email',
            field=models.EmailField(default='unknown@example.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='guestbookentry',
            name='author_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='guestbookentry',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='guestbookentry',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('blocked', 'Blocked')], max_length=10),
        ),
        migrations.AlterField(
            model_name='guestbookentry',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='guestbookentry',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]