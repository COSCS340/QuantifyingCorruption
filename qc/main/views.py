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

def search(request):
    context = {}
    print(dir(request))
    if request.method == "POST":
        query = request.POST['query']
        results = set()
        legislators = Legislator.objects.all()
        for filter_field in Legislator._meta.get_fields():
            for result in legislators.filter(**{filter_field.name + "__icontains": query}).all():
                results.add(result)
        print(results)
        context['results'] = list(results)
    else:
        context['results'] = list()
    return render(request, 'main/search.html', context)

def legislator(request, legislator_id):
    context = {}
    context['legislator'] = Legislator.objects.filter(id=legislator_id).get()
    print(context['legislator'].party)
    return render(request, 'main/legislator.html', context)

def about(request):
    context = {}
    return render(request, 'main/about.html', context=context)

def populate(request):
    context = { "success" : "success" }
    try:
        with open("../data/qc-working.csv", "r") as f:
            for line in f:
                l = Legislator(*[ line.split(",") ])
                l.save()
                pass
    except Exception as e:
        context["success"] = "Failed"
        context["error"] = str(e)

    return render(request, 'main/populate.html', context=context)


class SearchResult:
    def __init__(self, title, text, link):
        self.title = title
        self.text = text
        self.link = link
        return
