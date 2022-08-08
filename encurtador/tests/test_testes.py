import pytest
from django.urls import reverse
from encurtador.models import Links
from django.test.client import Client
from django.test import TestCase


def test_teste():
    teste = 11
    assert teste == 11


def test_StatusCode(client):
    response = client.get('')
    assert response.status_code == 200


# class TesteUm(TestCase):
def test_home_status_200():
    request = Client().get('')
    TestCase().assertTemplateUsed(request, 'encurtador/home.html')


@pytest.mark.django_db
def test_salvar_status_200():
    url = reverse('valida_link')
    Client().post(url, {'link_redirecionado': 'https://www.google.com', 'link_personalizado': ['1234']})
    assert Links.objects.count() == 1
