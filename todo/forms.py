from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from django import forms

from . models import Task


# creating a form 

# - Register a User

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


# - Login a User

class LoginForm(AuthenticationForm):
	username = forms.CharField(widget=TextInput())
	password = forms.CharField(widget=PasswordInput())


# - Create a Task

class CreateTaskForm(forms.ModelForm):
	
	class Meta:
		model = Task
		fields = ['title', 'content',]
		exclude = ['user',]
