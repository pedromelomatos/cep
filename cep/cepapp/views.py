from django.shortcuts import render, HttpResponse
from django.http import HttpRequest

# Create your views here.

def home(request:HttpRequest):
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == 'POST':
        inputcep = request.POST.get('cepinput') #pegando as infos do nosso input que veio do post lá do HTML
        infos_endereco = f'viacep.com.br/ws/{inputcep}/json/'
        print(infos_endereco)
        return render(request, 'home.html')