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


class Question(models.Model):
    question = models.CharField(max_length=500)
    date_added = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=1000)

    QTN_LANGUAGE = [
        ("py", "Python"),
        ("js", "Java script"),
        ("sh", "Shell"),
    ]

    language = models.CharField(max_length=2, choices=QTN_LANGUAGE)

    def __str__(self):
        return "<Language: {} ID {}>".format(self.language, self.id)


class Answer(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    answer = models.CharField(max_length=1000)
