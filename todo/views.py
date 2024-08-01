from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def home(request):
    
    clientlist = [
        {
            'id': '1',
            'name': 'Mamun Rashid',
            'profession' : 'Student'
        },

        {
            'id': '2',
            'name': 'Rony Reza',
            'profession' : 'Medicin Promotion Officer'
        },

        {
            'id': '3',
            'name': 'Milton',
            'profession' : 'HR'
        },
    ]

    context = {'client': clientlist}

    return render(request, 'index.html', context=context)


def register(request):
    return render(request, 'register.html')


def my_login(request):
    return render(request, 'my-login.html')
