import django_filters
from django import forms
from django.db import models
from django import template

from .models import Type,Article,Commande

# STATUS_CHOICES = ()
# def get_types():
#     types = Type.objects.all()
#     STATUS_CHOICES = ([(i.id, i.libelle) for i in types ])
#     return STATUS_CHOICES
class ListingFilter(django_filters.FilterSet):

    nom = forms.CharField(
            max_length=100,
            required = True,
            help_text='Enter First Name',
            widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'First Name'}),
            )
    # type=django_filters.ChoiceFilter(choices=get_types())
    
    class Meta:
        model = Article
        fields = {'nom' :  ['icontains'] , 'type' : ['exact']}
        # widget={'class': 'form-control', 'placeholder': 'Last Name'},
        

class CommandeFiler(django_filters.FilterSet):
    
    code = forms.CharField(
            max_length=100,
            required = True,
            help_text='Taper votre code !!!',
            widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'First Name'}),
            )
    # type=django_filters.ChoiceFilter(choices=get_types())
    
    class Meta:
        model = Commande
        fields = {'code' :  ['icontains'] , 'gouvernorat' : ['exact']}
        widget={
            'code': {'class': 'form-control', 'placeholder': 'Last Name'}},