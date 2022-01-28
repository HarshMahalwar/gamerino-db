from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from calc import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('create/', views.createRoom, name="create"),
    path('update/<str:pk>/', views.updateRoom, name="update"),
    path('delete/<str:pk>/', views.deleteRoom, name="delete")
]
