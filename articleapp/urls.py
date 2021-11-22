from django.urls import path

from articleapp.views import hello_world


app_name = 'articleapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]