from django import forms
from django.forms.widgets import MultiWidget

class signUpForms(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput({'placeholder': 'Enter you name'}))
    username = forms.CharField(required=True, widget=forms.TextInput({'placeholder': 'Set username'}))
    password = forms.CharField(required=True, widget=forms.TextInput({'placeholder': 'Set password'}))
    email = forms.EmailField(required=True, widget=forms.TextInput({'placeholder': 'Enter your email'}))


class loginForms(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput({'placeholder': 'Username'}))
    password = forms.CharField(required=True, widget=forms.TextInput({'placeholder': 'Password'}))

class uploadImageForms(forms.Form):
    image = forms.ImageField()