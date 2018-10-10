from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def index(response):
    return HttpResponse('<h1>Hello, myapp1!</h1>')
