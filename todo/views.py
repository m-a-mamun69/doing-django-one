from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import Task
# from .forms import InputForm
from .forms import CreateUserForm, LoginForm
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
            return HttpResponse('The User Is Created!!!')

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
    return render(request, 'dashboard.html')