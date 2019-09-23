from django.urls import path
from . import views

app_name = 'url'

urlpatterns = [
    path('', views.url_list, name='url_list'),
]
