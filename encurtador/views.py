from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import FormLinks
from.models import Links
from django.shortcuts import redirect 


def home(request):
    form = FormLinks()
    status = request.GET.get('status')
    return render(request, 'home.html', {'form': form, 'status':status})


def valida_link(request):
    form = FormLinks(request.POST)

    link_personalizado = form.data['link_personalizado']
    links = Links.objects.filter(link_personalizado = link_personalizado)
    if len(links) > 0:
        return redirect ("/?status=1")

    if form.is_valid():
       

        return HttpResponse(form.data['link_personalizado'])  