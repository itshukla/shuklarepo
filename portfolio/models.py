from djongo import models


class users(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=40)
    subject = models.CharField(max_length=30)
    message = models.TextField(max_length=255)
# Create your models here.
