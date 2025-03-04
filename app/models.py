from django.db import models

# Create your models here.

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=100, null=True, blank=True)
    reviewText = models.TextField(max_length=500)
    stars = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
