from django import forms

from expensapp.models import Expense

from django.contrib.auth.forms import  UserCreationForm

from expensapp.models import User



class SignUpForm(UserCreationForm):

    class Meta:
        model=User

        fields=["username","email","password1","password2","phone"]


class SignInForm(forms.Form):

    username=forms.CharField(max_length=20)

    password=forms.CharField(max_length=20)


class ExpenseForm(forms.ModelForm):

    class Meta:

        model=Expense

        fields="__all__"


class ExpenseUpdateForm(forms.ModelForm):

    class Meta:

        model=Expense

        fields=["title","category","amount","payment_method"]

