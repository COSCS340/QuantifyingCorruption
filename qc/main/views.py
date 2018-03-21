from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloworld(request):
    context = {}
    return render(request, 'main/hello.html', context)

def splash(request):
    context = {}
    return render(request, 'main/splash.html', context)
