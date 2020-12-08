from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Budget.models import Expenses

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]


class LoginForm(forms.Form):
    username=forms.CharField(max_length=120)
    password=forms.CharField(max_length=120)

class AddExpensForm(ModelForm):
    user=forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model=Expenses
        fields=["category","amount","note","user"]

class ReviewExpensesForm(forms.Form):
    user=forms.HiddenInput()
    from_date=forms.DateField(widget=forms.SelectDateWidget())
    to_date=forms.DateField(widget=forms.SelectDateWidget())




