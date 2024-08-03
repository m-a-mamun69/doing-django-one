
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home), 
    path('register', views.register), 
    path('my-login', views.my_login), 
    path('create-task', views.createTask),
]
