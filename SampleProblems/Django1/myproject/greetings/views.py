from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Welcome to the Greetings App!")

def greet_user(request, username):
    return HttpResponse(f"Hello, {username}!")

def say_goodbye(request, username):
    return HttpResponse(f"Goodbye, {username}!")
