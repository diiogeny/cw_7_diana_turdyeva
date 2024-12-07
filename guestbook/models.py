from django.db import models

class GuestbookEntry(models.Model):
    author_name = models.CharField(max_length=100)
    author_email = models.EmailField(default='unknown@example.com')
    text = models.TextField()
    email = models.EmailField(default='default@example.com')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=[('active', 'Active'), ('blocked', 'Blocked')]
    )
