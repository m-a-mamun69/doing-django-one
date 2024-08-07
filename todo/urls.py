
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home), 
    path('register', views.register), 
    path('my-login', views.my_login),
    # - CRUD Operations
    # - Create Task 
    path('create/', views.createTask),
    # - Read All Task
    path('view-tasks/', views.viewTask, name='view-tasks'),
]
