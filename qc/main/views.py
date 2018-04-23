from django.shortcuts import render
from django.http import HttpResponse
from .models import Legislator

import pandas as pd

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
    fields = ["identifier", "name", "party", "state", "donoSetOne", "donoSetTwo", "donoSetThree", "donoSetFour", "median", "individual", "pac" ]
    cav = None
    try:
        csv = pd.read_csv("../data/qc-working.csv")
    except Exception as e:
        context["error"] = [str(e)]
        return render(request, 'main/populate.html', context=context)

    for i,line in enumerate(csv.to_dict(orient='records')):
        try:
            l = Legislator(**line)
            l.save()
        except Exception as e:
            context["success"] = "Failed"
            if "error" not in context:
                context["error"] = []
            context["error"].append(str(e) + ("\t\tLine %d: " % i) + line)

    return render(request, 'main/populate.html', context=context)

def results(request):
    context = {}
    id = request.GET.get('id_name')
    if id is not None:
        dono = Legislator.objects.get(cand_id=id)
        context['results'] = dono
    print(context)
    return render(request, 'main/results.html', context=context)

class SearchResult:
    def __init__(self, title, text, link):
        self.title = title
        self.text = text
        self.link = link
        return
