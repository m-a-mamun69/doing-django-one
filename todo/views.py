from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
# from .forms import InputForm
from .forms import CreateUserForm, LoginForm, CreateTaskForm, UpdateUserForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):

    return render(request, 'index.html')


# - Registering / Create A User

def Register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form':form}
    return render(request, "register.html", context=context)


# - For Login A User

def my_login(request):
    form = LoginForm
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    context = {'form':form}
    return render(request, "my-login.html", context=context)


# - For Logout A User

def user_logout(request):
    auth.logout(request)
    return redirect('')


# - User Dashboard

@login_required(login_url='my-login')
def dashboard(request):
    return render(request, 'profile/dashboard.html')


# - Create A Task

@login_required(login_url='my-login')
def createTask(request):
    form = CreateTaskForm()

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            
            return redirect('dashboard')
    
    context = {'form':form}
    return render(request, "profile/create-task.html", context=context)


# - View All Tasks

@login_required(login_url='my-login')
def viewTask(request):

    current_user = request.user.id
    task = Task.objects.all().filter(user=current_user)
    context = {'task':task}
    return render(request, 'profile/view-tasks.html', context=context)


# - Update Tasks

@login_required(login_url='my-login')
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = CreateTaskForm(instance=task)

    if request.method == 'POST':
        form = CreateTaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('view-tasks')
    
    context = {'form':form}
    return render(request, 'profile/update-task.html', context=context)


# - Delete Tasks


def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('view-tasks')

    return render(request, 'profile/delete-task.html')



# - Profile Management

@login_required(login_url='my-login')
def profile_management(request):
    
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            return redirect('dashboard')

    user_form = UpdateUserForm(instance=request.user)
    context = {'user_form':user_form}
    return render(request, 'profile/profile-management.html', context=context)


