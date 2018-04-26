from django.shortcuts import render

# Create your views here.
 
def global_setting(request):
    return locals()


def index(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'index.html', context)

def agent(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'agent.html', context)

def blog(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'blog.html', context)


def contact(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'contact.html', context)
