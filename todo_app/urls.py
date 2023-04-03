from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('createToDo/', views.createToDo, name='createToDo'),
    path('updateToDo/<str:pk>/', views.updateToDo, name='updateToDo'),
    path('deleteToDo/<str:pk>/', views.deleteToDo, name='deleteToDo'),
]
