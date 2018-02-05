from django.shortcuts import render

# Create your views here.
def helloworld(request):
    context = {}
    return render(request, 'main/hello.html', context)
