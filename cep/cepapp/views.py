from django.shortcuts import render, HttpResponse
from django.http import HttpRequest
import requests
# Create your views here.

def home(request:HttpRequest):
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == 'POST':
        inputcep = request.POST.get('cepinput') #pegando as infos do nosso input que veio do post lá do HTML
        url = f'https://viacep.com.br/ws/{inputcep}/json/'
        request_cep = requests.get(url)
        infos_endereco = request_cep.json()
        return render(request, 'home.html', {'infos_endereco': infos_endereco})