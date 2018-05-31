from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as user_login
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model

from .models import Question, Answer
from .forms import RegisterForm, QuestionForm, AnswerForm


def index(request):
    return render(request, "user/index.html")


def login(request):
    return render(request, "registration/login.html")


def logout(request):
    return render(request, "registration/logout.html")


def questions(request):
    qtns = Question.objects.order_by("-date_added")
    context = {"qtns": qtns}
    return render(request, "user/questions.html", context)


def register(request):
    form = RegisterForm(request.POST)
    print(form.is_valid())
    if request.method == 'POST' and form.is_valid():
        form.save()
        username = form.cleaned_data['username']
        raw_password = form.cleaned_data['password1']
        new_user = authenticate(username=username, password=raw_password)
        user_login(request, new_user)
        return redirect("index")
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)


# def gists(request):
#     gists_posted = Gist.objects.order_by("-date_added")
#     context = {"gists_posted": gists_posted}
#     return render(request, "user/gists.html", context)


def profile(request):
    user_qtns = Question.objects.filter(login_user=request.user)
    context = {"user_qtns": user_qtns}
    return render(request, "user/profile.html", context)


def questioned(request):
    user_qtns = Question.objects.filter(login_user=request.user)
    context = {"user_qtns": user_qtns}
    return render(request, "user/questioned.html", context)


def answered(request):
    user_answered = Answer.objects.filter(login_user=request.user)

    qtns_answered = [(ans, Question.objects.get(id=ans.qtn_id))
                     for ans in user_answered]
    context = {"qtns_answered": qtns_answered}
    return render(request, "user/answered.html", context)


def question(request):
    form = QuestionForm(request.POST)
    print(form.is_valid())
    if request.method == 'POST' and form.is_valid():
        questn = form.save(commit=False)
        questn.login_user = request.user.username
        questn.save()
        return redirect("questions")
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'user/question.html', context)


def answer(request, qtn_id):
    form = AnswerForm(request.POST)
    print(form.is_valid())
    if request.method == 'POST' and form.is_valid():
        ans = form.save(commit=False)
        ans.login_user = request.user.username
        ans.qtn_id = qtn_id
        ans.save()
        return redirect("answer", qtn_id)
    else:
        qtn_asked = Question.objects.get(id=qtn_id)
        context = {"qtn": qtn_asked, "form": form}
        try:
            ans = list(Answer.objects.filter(qtn_id=qtn_id))
            context.update({"answered": ans})
        except Answer.DoesNotExist:
            pass
        form = AnswerForm()
    return render(request, 'user/answer.html', context)


# def create_gist(request):
#     form = GistForm(request.POST)
#     print(form.is_valid())
#     if request.method == 'POST' and form.is_valid():
#         gist_created = form.save(commit=False)
#         gist_created.user = request.user
#         gist_created.save()
#         return redirect("gists")
#     else:
#         form = GistForm()
#         context = {"form": form}
#     return render(request, 'user/create_gist.html', context)


# def gist_comments(request):
#     pass


# def snippets(request):
#     pass


# def register(request):
#     form = UserCreationForm(request.POST)
#     print(form.is_valid())
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         username = form.cleaned_data['username']
#         raw_password = form.cleaned_data['password1']
#         new_user = authenticate(username=username, password=raw_password)
#         user_login(request, new_user)
#         return redirect("index")
#     else:
#         form = UserCreationForm()
#     context = {'form': form}
#     return render(request, 'registration/register.html', context)
