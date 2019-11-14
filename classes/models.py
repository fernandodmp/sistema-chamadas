from django.db import models
from users.models import Person
from datetime import date

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=300, blank=True)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    participants = models.ManyToManyField(
        Person, related_name="participants", blank=True)
    access_key = models.CharField(max_length = 12, blank = True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    on_going = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True)
    attendants = models.ManyToManyField(
        Person, related_name="attendants", blank=True)
    auth_code = models.CharField(max_length=6)

    def __str__(self):
        if self.date:
            return str(self.date.day) + "/" + str(self.date.month) + "/" + str(self.date.year)
