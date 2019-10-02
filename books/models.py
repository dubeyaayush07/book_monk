from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    for_rent = models.BooleanField()
    for_sale = models.BooleanField()
    date_posted = models.DateTimeField(default=timezone.now)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})