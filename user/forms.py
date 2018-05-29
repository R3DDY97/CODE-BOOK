
from django import forms
# from django.forms import formset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Question, Answer


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True,
                                 help_text='Enter your first name.')
    last_name = forms.CharField(max_length=30, required=True,
                                help_text='Enter your last name.')

    birth_date = forms.DateField(required=True,
                                 help_text='Required. Format: YYYY-MM-DD')

    email = forms.EmailField(max_length=254, required=True,
                             help_text="Required. Needs valid email id")

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'birth_date', 'username',
                  'email', 'password1', 'password2', )


class QuestionForm(forms.ModelForm):

    qtn = {"class": "input is-large is-primary",
                    "placeholder": "Enter your question",
           }

    question = forms.CharField(max_length=500, required=True,
                               widget=forms.TextInput(attrs=qtn))

    descript = {"class": "textarea is-primary",
                "placeholder": "Describe about your question",
                "rows": "5"}

    description = forms.CharField(widget=forms.Textarea(attrs=descript),
                                  max_length=1000, required=True)

    QTN_LANGUAGE = [
        ("py", "Python"),
        ("js", "Java script"),
        ("sh", "Shell"),
    ]

    language = forms.ChoiceField(required=True,
                                 widget=forms.Select,
                                 choices=QTN_LANGUAGE)

    class Meta:
        model = Question
        fields = ["question", "description", "language"]


class AnswerForm(forms.ModelForm):

    ans = {"class": "textarea is-primary",
           "placeholder": "Enter answer",
           "rows": "5"}

    answer = forms.CharField(widget=forms.Textarea(attrs=ans),
                             required=True)

    class Meta:
        model = Answer
        fields = ["answer"]
