from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, UserC, School

class RegistrationForm(UserCreationForm):
    school = forms.ModelChoiceField(label='School', queryset=School.objects.all(), empty_label='Select a school')

    class Meta:
        model = UserC
        fields = ['username', 'password1', 'password2', 'school']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']