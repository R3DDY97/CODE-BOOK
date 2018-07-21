from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.register, name="register"),
    path("question/", views.question, name="question"),
    path("questions/", views.questions, name="questions"),
    path("answer_<qtn_id>/", views.answer, name="answer"),
    path("profile/", views.profile, name="profile"),
    path("questioned/", views.questioned, name="questioned"),
    path("answered/", views.answered, name="answered"),

    # path("gists/", views.gists, name="gists"),
    # path("create_gist/", views.create_gist, name="create_gist"),
    # path("gist_comments/", views.gist_comments, name="gist_comments"),
    # path("snippets/", views.snippets, name="snippets"),

]
