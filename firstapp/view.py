from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1>Hello, World! This is my first Django app!</h1>")