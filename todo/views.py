from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("This My Home Page For this Projects")


def register(request):
    return HttpResponse("This My Register Page For this Projects")


def my_login(request):
    return HttpResponse("This My Login Page For this Projects")
