from django import forms
from django.forms import fields
from .models import Links


class FormLinks(forms.ModelForm):
    class Meta:
        model = Links
        fields = ['linkredirecionado', 'link_personalizado']
