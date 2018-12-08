from django import forms
from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
