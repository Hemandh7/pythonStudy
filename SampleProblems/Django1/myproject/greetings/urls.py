from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('greet/<str:username>/', views.greet_user, name='greet'),
    path('farewell/<str:username>/', views.say_goodbye, name='farewell'),
]
