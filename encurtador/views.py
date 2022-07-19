from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormLinks
from .models import Links
from django.shortcuts import redirect


def home(request):
    form = FormLinks()
    status = request.GET.get('status')
    return render(request, 'home.html', {"form": form, "status": status})


def valida_link(request):
    form = FormLinks(request.POST)
    host = request.META.get('HTTP_HOST')

    link_personalizado = form.data['link_personalizado']
    #links = Links.objects.filter(link_personalizado=link_personalizado)

    if not form.is_valid():
        # return HttpResponse("Formulário invalido")
        return render(request, 'existente.html')
    try:
        form.save()
        # return render("meu-template-links-adicionado!")
        # return HttpResponse(f"Seu link foi criado com sucesso e é: {host}/{form.data['link_personalizado']}")
        new_link = f"{host}/{form.data['link_personalizado']}"
        abrir_link = f"/{form.data['link_personalizado']}"
        contex = {
            'new_link': new_link,
            'abrir_link': abrir_link,
        }
        return render(request, 'sucesso.html', contex)

    except Exception as error:
        raise Exception("algum erro no salvar!")


def redirecionar(request, link):
    links = Links.objects.filter(link_personalizado=link)
    if len(links) == 0:
        # return render("pagina404")
        # return redirect('/')
        return render(request, '404.html')

    return redirect(links[0].link_redirecionado)
