from django.shortcuts import render
from django.http import HttpResponse
from keijiban.forms import KakikomiForm

# Create your views here.
def kakikomi(request):
    f = KakikomiForm({
        'name' : ' hide',
        'email' : 'hide@example.com',
        'body' : 'Hello this is django form'}
        )
    # return HttpResponse(f.as_table())
    return render(request, 'keijiban/kakikomiform.html', {'form1': f} )
