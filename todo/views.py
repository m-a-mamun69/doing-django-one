from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
# from .forms import InputForm
from .forms import TaskForm

# Create your views here.

def home(request):

    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')


def my_login(request):
    return render(request, 'my-login.html')


def createTask(request):

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('Your task was Created!')
    context = {'form':form}
    return render(request, "create.html", context=context)

    # form = TaskForm()
    # if request.method == 'POST':
        
    #     form = TaskForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponse('Your task was Created!')

    # context = {'from':form}
    # return render(request, 'create-task.html', context=context)
