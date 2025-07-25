from django.shortcuts import render, HttpResponse
from django.http import HttpRequest

# Create your views here.

def home(request:HttpRequest):
    if request.method == 'GET':
        return render(request, 'home.html')