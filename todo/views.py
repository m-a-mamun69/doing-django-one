from django.shortcuts import render
# from django.http import HttpResponse
from .models import Task

# Create your views here.

def home(request):
    queryAllData = Task.objects.all()
    context = {'tasks': queryAllData}

    return render(request, 'index.html', context)


def register(request):
    return render(request, 'register.html')


def my_login(request):
    return render(request, 'my-login.html')
