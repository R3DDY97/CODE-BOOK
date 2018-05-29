from django.db import models
from django.utils import timezone


class Users(models.Model):
    username = models.CharField(max_length=256)

    def __str__(self):
        return "<Username: {} ID: {}>".format(self.username, self.id)


class Registered(models.Model):
    username = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    dob = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "<Username: {} ID: {}>".format(self.username, self.id)
