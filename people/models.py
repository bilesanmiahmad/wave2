from django.db import models

# Create your models here.
class People(models.Model):
    email = models.EmailField(max_length=70, blank=False, null=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)