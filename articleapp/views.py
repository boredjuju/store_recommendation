from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from articleapp.models import history, stores


def hello_world(request):
    return render(request, 'articleapp/hello_world.html')

def index(request):

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

        print(menu_input, addr_input, region_input)
        print(type(addr_input))
        print('zzzzzz')
        print(f' addr_input : {type(addr_input)}, menu_input : {type(menu_input)}')

        if (menu_input == '') & (addr_input == ''):
            store_list = stores.objects.filter(Q(region=region_input)).order_by('-pick_avg_score')


        elif (menu_input == '') & (addr_input != ''):
            store_list = stores.objects.filter(Q(region=region_input) &
                                               Q(store_addr__contains=addr_input)).order_by('-pick_avg_score')

        elif (addr_input != '') & (menu_input == ''):
            store_list = stores.objects.filter(Q(region=region_input) &
                                               Q(menu=menu_input)).order_by('-pick_avg_score')

        else:
            store_list = stores.objects.filter(Q(region=region_input) &
                                               Q(menu=menu_input) &
                                               Q(store_addr__contains=addr_input)).order_by('-pick_avg_score')



        context = {'history_output': new_history, 'store_list': store_list}

        return render(request, 'articleapp/search.html', context)
    else:
        return render(request, 'articleapp/search.html')

class StoreListView(ListView):
    model = stores
    templates = "articleapp/search.html"
    context_object_name = "context"
    paginate_by = 10  #the number of stores per page

    def get_context_data(self, **kwargs):
        if self.request.method == 'POST':
            addr_input = self.request.POST.get('addr_input')
            region_input = self.request.POST.get('region_input')
            menu_input = self.request.POST.get('menu_input')

            new_history = history()
            new_history.menu = menu_input
            new_history.addr = addr_input
            new_history.region = region_input
            new_history.save()

            if (menu_input == '') & (addr_input == ''):
                store_list = stores.objects.filter(Q(region=region_input)).order_by('-pick_avg_score')


            elif (menu_input == '') & (addr_input != ''):
                store_list = stores.objects.filter(Q(region=region_input) &
                                                   Q(store_addr__contains=addr_input)).order_by('-pick_avg_score')

            elif (addr_input != '') & (menu_input == ''):
                store_list = stores.objects.filter(Q(region=region_input) &
                                                   Q(menu=menu_input)).order_by('-pick_avg_score')

            else:
                store_list = stores.objects.filter(Q(region=region_input) &
                                                   Q(menu=menu_input) &
                                                   Q(store_addr__contains=addr_input)).order_by('-pick_avg_score')

            context = {'history_output': new_history, 'store_list': store_list}
        return context

