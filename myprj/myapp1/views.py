from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('<h1>Hello, myapp1!</h1>')
    return render(request, 'myapp1/index.html')
