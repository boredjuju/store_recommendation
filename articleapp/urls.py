from django.urls import path

from articleapp.views import hello_world, index, search, StoreListView



app_name = 'articleapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('index/', index, name='index'),
    path('search/', search, name='search'),
    # path('search/', StoreListView.as_view(), name='search'),
]