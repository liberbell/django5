from django.shortcuts import render
from django.http import HttpResponse
from keijiban.forms import KakikomiForm
from myapp1.forms import LoginForm

# Create your views here.
def kakikomi(request):
    # f = KakikomiForm({
    #     'name' : ' hide',
    #     'email' : 'hide@example.com',
    #     'body' : 'Hello this is django form'}
    #     )
    # return HttpResponse(f.as_table())
    # return render(request, 'keijiban/kakikomiform.html', {'form1': f} )
    if request.method == 'post':
        f = KakikomiForm(request.POST)
    else:
        f = KakikomiForm()
    return render(
        request,
        'keijiban/kakikomiform.html',
        {'form1' : f}
    )

def index(request):
    return render(request, 'myapp1/index.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if username == 'user1' and password == 'secret':
                return HttpResponseRedirect('/myapp1/')
            else:
                return render(request, 'myapp1/login.html',
                {
                    'form':from,
                    'mag':'Authentication failed'
                })
