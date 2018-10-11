from django.shortcuts import render
from django.http import HttpResponse
from keijiban.form import KakikomiForm

# Create your views here.
def kakikomi(request):
    f = KakikomiForm()
    return HttpResponse(f)
