from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# from captcha.fields import CaptchaField
from django import forms
from application.models import Upload, JsonData


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = "__all__"


class JDataForm(forms.ModelForm):
    class Meta:
        model = JsonData
        fields = "__all__"