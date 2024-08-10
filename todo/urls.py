
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home), 
    path('register', views.register), 
    path('my-login', views.my_login),

    # ---------- CRUD Operations ----------- #

    # - Create Task 
    path('create/', views.createTask, name='create'),
    # - Read All Task
    path('view-tasks/', views.viewTask, name='view-tasks'),
    # - Update Task
    path('update-task/<str:pk>/', views.updateTask, name='update-task'),
    # - Update Task
    path('delete-task/<str:pk>/', views.deleteTask, name='delete-task'),

        # ---------- Authentications Operations ----------- #
        # ------------------------------------------------- #

    # - Registrations
    path('register/', views.Register, name='register'),
    # - Login Url
    path('my-login/', views.my_login, name='my-login'),
]
