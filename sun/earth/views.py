from django.shortcuts import render

# Create your views here.
 
def global_setting(request):
    return locals()


def index(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'index.html', context)

def savePhoneNum(request):
    pass
