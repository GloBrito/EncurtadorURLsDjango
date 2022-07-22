from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormLinks
from .models import Links
from django.shortcuts import redirect


def home(request):
    form = FormLinks()
    status = request.GET.get('status')
    return render(request, 'encurtador/home.html', {"form": form, "status": status})


def valida_link(request):
    form = FormLinks(request.POST)
    host = request.META.get('HTTP_HOST')

    link_personalizado = form.data['link_personalizado']

    if not form.is_valid():
        new_link = f"{form.data['link_redirecionado']}"
        abrir_link = f"encurteco.herokuapp.com/{form.data['link_personalizado']}"
        contex = {
            'new_link': new_link,
            'abrir_link': abrir_link,
        }
        return render(request, 'encurtador/existente.html', contex)
    try:
        form.save()
        new_link = f"{host}/{form.data['link_personalizado']}"
        abrir_link = f"/{form.data['link_personalizado']}"
        contex = {
            'new_link': new_link,
            'abrir_link': abrir_link,
        }
        return render(request, 'encurtador/sucesso.html', contex)

    except Exception as error:
        raise Exception("algum erro no salvar!")


def redirecionar(request, link):
    links = Links.objects.filter(link_personalizado=link)
    if len(links) == 0:
        return render(request, 'encurtador/404.html')

    return redirect(links[0].link_redirecionado)
