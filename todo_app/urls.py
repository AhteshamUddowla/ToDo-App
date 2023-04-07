from django.urls import path
from . import views

urlpatterns = [

    path('', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('account/<str:pk>/', views.userAccount, name='account'),

    path('todo/', views.createToDo, name='todo'),
    # path('createToDo/', views.createToDo, name='createToDo'),
    path('updateToDo/<str:pk>/', views.updateToDo, name='updateToDo'),
    path('deleteToDo/<str:pk>/', views.deleteToDo, name='deleteToDo'),
]
