from django.shortcuts import render, get_object_or_404
from .models import Link
from .forms import LinkForm


# Create your views here.
def url_list(request):
    object_list = Link.objects.order_by('-created').all()
    return render(request, 'url/list.html', {'links': object_list})


def add_link(request):
    if request.method == 'POST':
        # Пользователь отправил комментарий.
        link_form = LinkForm(data=request.POST)
        if link_form.is_valid():
            link_form.save()

    link_form = LinkForm()
    return render(request, 'url/add.html', {'link_form': link_form})
