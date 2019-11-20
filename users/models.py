from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Person(AbstractUser):

    username = models.CharField(max_length=40, unique=False, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
