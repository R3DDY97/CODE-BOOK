from django.contrib import admin
from .models import Users, Registered, Question, Answer

admin.site.register(Users)
admin.site.register(Registered)
admin.site.register(Question)
admin.site.register(Answer)
