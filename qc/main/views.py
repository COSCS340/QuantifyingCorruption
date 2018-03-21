from django.shortcuts import render
from django.http import HttpResponse
from .models import Legislator

# Create your views here.
def helloworld(request):
    context = {}
    return render(request, 'main/hello.html', context)

def splash(request):
    context = {}
    return render(request, 'main/splash.html', context)

def legislator(request, legislator_id):
    context = {}
    context['legislator'] = Legislator.objects.filter(id=legislator_id).get()
    print(context['legislator'].party)
    return render(request, 'main/legislator.html', context)
