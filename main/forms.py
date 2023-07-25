from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'intro', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Article title"
            }),
            "intro": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Article introduction"
            }),
            "date": DateTimeInput(attrs={
                "class": "form-control",
                "placeholder": "Date of publication"
            }),
            "full_text": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Full Article"
            })
        }



class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]