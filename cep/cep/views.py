from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpRequest

def redirecionar(request:HttpRequest):
    return redirect('cepapp:home')