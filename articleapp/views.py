from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world(request):
    return render(request, 'articleapp/hello_world.html')

def index(request):

    if request.method == 'POST':

        temp = request.POST.get('addr_input')

        return render(request, 'articleapp/index.html', context={'text': 'POST METHOD!!!'})
    else:
        return render(request, 'articleapp/index.html', context={'text': 'GET METHOD!!!'})

def search(request):
    return render(request, 'articleapp/search.html')