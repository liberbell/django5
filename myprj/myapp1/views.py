from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    # return HttpResponse('<h1>Hello, myapp1!</h1>')
    template = loader.get_template('myapp/index.html')
    context = {'fname':'hide'}
    return HttpResponse(template.render( context, request))
    # return render(request, 'myapp1/index.html')
