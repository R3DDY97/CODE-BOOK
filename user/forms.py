
from django import forms
# from django.forms import formset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Question, Answer


class RegisterForm(UserCreationForm):

    fname_attr = {"placeholder": "First name"}
    lname_attr = {"placeholder": "Last name"}
    date_attr = {"placeholder": "YYYY-MM-DD"}
    email_attr = {"placeholder": "Need valid email-id"}

    first_name = forms.CharField(max_length=30, required=True,
                                 widget=forms.TextInput(attrs=fname_attr))

    last_name = forms.CharField(max_length=30, required=True,
                                widget=forms.TextInput(attrs=lname_attr))

    birth_date = forms.DateField(required=True,
                                 widget=forms.TextInput(attrs=date_attr))

    email = forms.EmailField(max_length=254, required=True,
                             widget=forms.TextInput(attrs=email_attr))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'birth_date', 'username',
                  'email', 'password1', 'password2', )


class QuestionForm(forms.ModelForm):

    qtn_attr = {"class": "input is-medium is-primary",
                "placeholder": "Enter your question",
                }

    question = forms.CharField(max_length=500, required=True,
                               widget=forms.TextInput(attrs=qtn_attr))

    descript = {"class": "textarea is-primary",
                "placeholder": "Describe in detail about it",
                "rows": "5"}

    description = forms.CharField(widget=forms.Textarea(attrs=descript),
                                  max_length=1000, required=True)

    QTN_LANGUAGE = [
        ("python", "Python"),
        ("javascript", "Java script"),
        ("shell", "Shell"),
    ]

    language = forms.ChoiceField(required=True,
                                 widget=forms.Select,
                                 choices=QTN_LANGUAGE)

    class Meta:
        model = Question
        fields = ["question", "description", "language"]


class AnswerForm(forms.ModelForm):

    ans_attr = {"class": "textarea is-primary",
                "placeholder": "Enter answer",
                "rows": "5"}

    answer = forms.CharField(required=True,
                             widget=forms.Textarea(attrs=ans_attr))

    class Meta:
        model = Answer
        fields = ["answer"]


class GistForm(forms.ModelForm):

    name_attr = {"class": "input is-large is-primary",
                 "placeholder": "Name your gist code",
                 }

    gist_name = forms.CharField(max_length=500, required=True,
                                widget=forms.TextInput(attrs=name_attr))

    code_attr = {"class": "textarea is-primary",
                 "placeholder": "Describe in detail about it",
                 "rows": "5"}

    gist_code = forms.CharField(widget=forms.Textarea(attrs=code_attr),
                                max_length=1000, required=True)

    GIST_LANGUAGE = [
        ("python", "Python"),
        ("javascript", "Java script"),
        ("shell", "Shell"),
    ]

    language = forms.ChoiceField(required=True,
                                 widget=forms.Select,
                                 choices=GIST_LANGUAGE)

    class Meta:
        model = Question
        fields = ["gist_name", "gist_code", "language"]
