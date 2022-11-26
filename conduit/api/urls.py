from django.urls import path
from . import views

urlpatterns = [
    #Get all people
    path('', views.getAll, name='getUsers'),
    #Get one person
    path('user/<int:pk>/', views.getUser, name='getUser'),
    #add a person
    path('user/', views.addUser, name='addUser'),
    #update a person
    path('user/<int:pk>/update', views.updateUser, name='updateUser'),
    #delete a person
    path('user/<int:pk>/delete/', views.deleteUser, name='deleteUser'),

]
