
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''), 
        # ---------- Authentications Operations ----------- #
        # ------------------------------------------------- #
    # - Dashboard Url
    path('dashboard/', views.dashboard, name='dashboard'),

    # - Registrations
    path('register/', views.Register, name='register'),

    # - Login Url
    path('my-login/', views.my_login, name='my-login'),

    # - Logout Url
    path('user-logout/', views.user_logout, name='user-logout'),

    # - Create Task 
    path('create-task/', views.createTask, name='create-task'),

    # - Read All Task
    path('view-tasks/', views.viewTask, name='view-tasks'),

    # - Update Task
    path('update-task/<str:pk>/', views.updateTask, name='update-task'),
]


    # # ---------- CRUD Operations ----------- #

    # # - Create Task 
    # path('create/', views.createTask, name='create'),
    # # - Read All Task
    # path('view-tasks/', views.viewTask, name='view-tasks'),
    # # - Update Task
    # path('update-task/<str:pk>/', views.updateTask, name='update-task'),
    # # - Update Task
    # path('delete-task/<str:pk>/', views.deleteTask, name='delete-task'),