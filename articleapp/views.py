from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from articleapp.models import history, stores
import pandas as pd

def hello_world(request):
    return render(request, 'articleapp/hello_world.html')

def index(request):
    #
    # print('view')
    # df = pd.read_csv('C:/Users/hy949/PycharmProjects/store_recommendation/articleapp/final_info.csv', encoding='utf-8')
    # # print(len(df))
    # for i in range(len(df)):
    #     new_store= stores()
    #     new_store.id = df.loc[i][0]
    #     new_store.store_id = df.loc[i][1]
    #     new_store.region = df.loc[i][2]
    #     new_store.store_name = df.loc[i][3]
    #     new_store.store_x = df.loc[i][4]
    #     new_store.store_y = df.loc[i][5]
    #     new_store.store_addr = df.loc[i][6]
    #     new_store.store_addr_new = df.loc[i][7]
    #     new_store.store_tel = df.loc[i][8]
    #     new_store.open_hours = df.loc[i][9]
    #     new_store.website = df.loc[i][10]
    #     new_store.s_link = df.loc[i][11]
    #     new_store.siksin_avg_score = df.loc[i][12]
    #     new_store.dining_avg_score = df.loc[i][13]
    #     new_store.google_avg_score = df.loc[i][14]
    #     new_store.naver_avg_score = df.loc[i][15]
    #     new_store.pick_avg_score = df.loc[i][16]
    #     new_store.menu = df.loc[i][17]
    #
    #     new_store.save()
    #     print(i)
    #     #

    return render(request, 'articleapp/index.html')

# def search(request):
#     if request.method == 'POST':
#
#         addr_input = request.POST.get('addr_input')
#         region_input = request.POST.get('region_input')
#         menu_input = request.POST.get('menu_input')
#
#         new_history = history()
#         new_history.menu = menu_input
#         new_history.addr = addr_input
#         new_history.region = region_input
#         new_history.save()
#
#         print(menu_input, addr_input, region_input)
#         print(type(addr_input))
#         print('zzzzzz')
#         print(f' addr_input : {type(addr_input)}, menu_input : {type(menu_input)}')
#
#         if (menu_input == '') & (addr_input == ''):
#             store_list = stores.objects.filter(Q(region=region_input)).order_by('-pick_avg_score')
#
#
#         elif (menu_input == '') & (addr_input != ''):
#             store_list = stores.objects.filter(Q(region=region_input) &
#                                                Q(store_addr__contains=addr_input)).order_by('-pick_avg_score')
#
#         elif (addr_input != '') & (menu_input == ''):
#             store_list = stores.objects.filter(Q(region=region_input) &
#                                                Q(menu=menu_input)).order_by('-pick_avg_score')
#
#         else:
#             store_list = stores.objects.filter(Q(region=region_input) &
#                                                Q(menu=menu_input) &
#                                                Q(store_addr__contains=addr_input)).order_by('-pick_avg_score')
#
#
#
#         context = {'history_output': new_history, 'store_list': store_list}
#
#         return render(request, 'articleapp/search.html', context)
#     else:
#         return render(request, 'articleapp/search.html')

class StoreListView(ListView):
    model = stores
    template_name = "articleapp/search.html"
    context_object_name = "store_list"
    paginate_by = 10  #the number of stores per page

    # def get(self, request):
    #
    #     region_input = request.GET.get('region_input')
    #     addr_input = request.GET.get('addr_input')
    #     menu_input = request.GET.get('menu_input')
    #
    #     if not addr_input or not menu_input:
    #         addr_input = ""
    #         menu_input = ""
    #     new_history = history()
    #     new_history.menu = menu_input
    #     new_history.addr = addr_input
    #     new_history.region = region_input
    #     new_history.save()
    #
    #     if (menu_input == '') & (addr_input == ''):
    #         store_list = stores.objects.filter(Q(region=region_input)).order_by('-pick_avg_score')
    #
    #
    #     elif (menu_input == '') & (addr_input != ''):
    #         store_list = stores.objects.filter(Q(region=region_input) &
    #                                            Q(store_addr__contains=addr_input)).order_by('-pick_avg_score')
    #
    #     elif (addr_input != '') & (menu_input == ''):
    #         store_list = stores.objects.filter(Q(region=region_input) &
    #                                            Q(menu=menu_input)).order_by('-pick_avg_score')
    #
    #     else:
    #         store_list = stores.objects.filter(Q(region=region_input) &
    #                                            Q(menu=menu_input) &
    #                                            Q(store_addr__contains=addr_input)).order_by('-pick_avg_score')
    #     paginator = Paginator(store_list, 10)
    #     page_number = self.request.GET.get('page')
    #
    #     page_obj = paginator.get_page(page_number)
    #
    #     print(f'type : {type(page_number)}, value : {page_number}')
    #
    #     page_val = int(page_number)
    #
    #     context = {
    #         'page_obj': page_obj,
    #         "store_list": store_list[(page_val-1) * 10 : page_val*10],
    #         'region_input': region_input
    #     }
    #     # return render(request, 'articleapp/search.html', context={'store_list':store_list})
    #     return render(self.request, self.template_name, context)


    def get_queryset(self):
        addr_input = self.request.GET.get('addr_input')
        region_input = self.request.GET.get('region_input')
        menu_input = self.request.GET.get('menu_input')

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
                                               Q(menu__contains=menu_input)).order_by('-pick_avg_score')

        else:
            store_list = stores.objects.filter(Q(region=region_input) &
                                               Q(menu__contains=menu_input) &
                                               Q(store_addr__contains=addr_input)).order_by('-pick_avg_score')

        # context= { 'store_list' : store_list, 'region_inpit' : region_input}
        return store_list


    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     context['store_list'] = self.get_queryset()
    #
    # def get_query_string(self):
    #     pass
