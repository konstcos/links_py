from django.shortcuts import render, get_object_or_404
from .models import Link


# Create your views here.
def url_list(request):
    object_list = Link.objects.all()
    return render(request, 'url/list.html', {'links': object_list})
