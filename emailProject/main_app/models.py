from django.db import models

# Create your models here.


class EmailInfo(models.model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    emailAdress = models.EmailField(unique=True)