from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
# from django.conf import settings
# from django.db.models import (Count, Sum, Case, When, Value, IntegerField)


class Answer(models.Model):
    qtn_id = models.IntegerField(default=1)
    login_user = models.CharField(max_length=25, default=1)
    date_added = models.DateTimeField(default=timezone.now)
    answer = models.CharField(max_length=1000)

    def __str__(self):
        return "<id {}>".format(self.id)


class Question(models.Model):
    login_user = models.CharField(max_length=25, default=1)
    question = models.CharField(max_length=500)
    date_added = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=1000)
    QTN_LANGUAGE = [
        ("python", "Python"),
        ("javascript", "Java script"),
        ("shell", "Shell"),
        ("git", "Git"),
    ]

    language = models.CharField(max_length=10, choices=QTN_LANGUAGE)

    def __str__(self):
        return "<Language: {} ID {}>".format(self.language, self.id)


# class Gist(models.Model):
#     login_user = models.CharField(max_length=25, default=1)
#     date_added = models.DateTimeField(default=timezone.now)
#     gist_name = models.CharField(max_length=500)
#     gist_code = models.CharField(max_length=10000)
#     GIST_LANGUAGE = [
#         ("python", "Python"),
#         ("javascript", "Java script"),
#         ("shell", "Shell"),
#     ]

#     language = models.CharField(max_length=10, choices=GIST_LANGUAGE)

#     def __str__(self):
#         return "<{}-{}>".format((self.gist_code + self.gist_name)[:30],
#                                 self.id)
