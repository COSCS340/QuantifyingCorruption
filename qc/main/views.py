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

def search(request, query):
    context = {}
    results = set()
    legislators = Legislator.objects.all()
    for filter_field in Legislator._meta.get_fields():
        for result in legislators.filter(**{filter_field.name + "__icontains": query}).all():
            results.add(result)
    print(results)
    context['results'] = list(results)
    return render(request, 'main/search.html', context)

def legislator(request, legislator_id):
    context = {}
    context['legislator'] = Legislator.objects.filter(id=legislator_id).get()
    print(context['legislator'].party)
    return render(request, 'main/legislator.html', context)

class SearchResult:
    def __init__(self, title, text, link):
        self.title = title
        self.text = text
        self.link = link
        return
