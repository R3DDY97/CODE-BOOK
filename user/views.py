

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as user_login
# from django.contrib.auth.forms import UserCreationForm

from .models import Question, Answer
from .forms import RegisterForm, QuestionForm, AnswerForm


def index(request):
    return render(request, "user/index.html")


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


def login(request):
    return render(request, "registration/login.html")


def logout(request):
    return render(request, "registration/logout.html")


def questions(request):
    qtns = Question.objects.order_by("-date_added")
    context = {"qtns": qtns}
    return render(request, "user/questions.html", context)


# def answers(request):
#     ans = Answer.objects.order_by("-date_added")
#     context = {"answers": ans}
#     return render(request, "user/answer.html", context)


def question(request):
    form = QuestionForm(request.POST)
    print(form.is_valid())
    if request.method == 'POST' and form.is_valid():
        questn = form.save(commit=False)
        questn.user = request.user
        questn.save()
        return redirect("questions")
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'user/question.html', context)


def answer(request):
    form = AnswerForm(request.POST)
    print(form.is_valid())
    if request.method == 'POST' and form.is_valid():
        ans = form.save(commit=False)
        ans.user = request.user
        ans.save()
        return redirect("answer")
    else:
        ans = Answer.objects.order_by("-date_added")
        form = AnswerForm()
        context = {"answered": ans, "form": form}
    return render(request, 'user/answer.html', context)


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
