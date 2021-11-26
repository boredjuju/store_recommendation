from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from articleapp.models import history


def hello_world(request):
    return render(request, 'articleapp/hello_world.html')

def index(request):

    if request.method == 'POST':

        addr_input = request.POST.get('addr_input')
        region_input = request.POST.get('region_input')
        menu_input = request.POST.get('menu_input')

        new_history = history()
        new_history.menu = menu_input
        new_history.addr = addr_input
        new_history.region = region_input
        new_history.save()

        return render(request, 'articleapp/search.html', context={'history_output': new_history})
    else:
        return render(request, 'articleapp/index.html')

def search(request):
    if request.method == 'POST':

        addr_input = request.POST.get('addr_input')
        region_input = request.POST.get('region_input')
        menu_input = request.POST.get('menu_input')

        new_history = history()
        new_history.menu = menu_input
        new_history.addr = addr_input
        new_history.region = region_input
        new_history.save()

        return render(request, 'articleapp/search.html', context={'history_output': new_history})
    else:
        return render(request, 'articleapp/search.html')