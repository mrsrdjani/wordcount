from django.http import HttpResponse
from django.shortcuts import render

def eggs(request):
    return HttpResponse('Hello')

def pocetna(request):
    return render(request, 'home.html', {'hithere': 'This is me'})

def onama(request):
    return render(request, 'about.html')