from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False,
                                 help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False,
                                help_text='Optional.')

    birth_date = forms.DateField(required=True,
                                 help_text='Required. Format: YYYY-MM-DD')

    email = forms.EmailField(max_length=254, required=True,
                             help_text="Required. Needs valid email id")

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'birth_date', 'username',
                  'email', 'password1', 'password2', )
