from django import forms
from django.contrib.auth.models import User
import django_filters
from django.contrib.auth.forms import AuthenticationForm, UsernameField,UserCreationForm
from .models import Fournisseur,Commande,Gouvernorat
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from.widgets import DateTimeInput
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
        'username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'check',
        ]
    email = forms.EmailField(
    max_length=100,
    required = True,
    help_text='Enter Email Address',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )
    first_name = forms.CharField(
    max_length=100,
    required = True,
    help_text='Enter First Name',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
    )
    last_name = forms.CharField(
    max_length=100,
    required = True,
    help_text='Enter Last Name',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
    )
    username = forms.CharField(
    max_length=200,
    required = True,
    help_text='Enter Username',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    )
    password1 = forms.CharField(
    help_text='Enter Password',
    required = True,
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
    required = True,
    help_text='Enter Password Again',
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
    )
    check = forms.BooleanField(required = True)
    
class FournisseurForm(forms.ModelForm):
    
    class Meta:
        model= Fournisseur
        fields= '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'addresse': forms.TextInput(attrs={'class': 'form-control'}),
            'gouvernorat': forms.Select(attrs={'class': 'form-control'}),
            'contact' : forms.TextInput(attrs={'class': 'form-control'}),
            'telephone' : forms.TextInput(attrs={'class': 'form-control'}),
            'ville': forms.Select(attrs={'class': 'form-control'}),

        }
        
def get_gouvernorat():
    types = Gouvernorat.objects.all()
    STATUS_CHOICES = ([(i.id, i.libelle) for i in types ])
    return STATUS_CHOICES


        
class CommandeForm(forms.ModelForm):
    class Meta:
        model= Commande
        fields= '__all__'
        exclude = ('code','note','degustateurs')
        widgets = {
            'qte': forms.NumberInput(attrs={'class': 'form-control'}),
            #'fournisseur': forms.Select(attrs={'class': 'form-control'},choices=User.objects.filter(groups__name='fournisseur')),
            'gouvernorat': forms.Select(attrs={'class': 'form-control'}),
            'dateEchantion': DateTimeInput(attrs={'class': 'form-control'}),
            'code_pile': forms.TextInput(attrs={'class': 'form-control'} ),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'cellage': forms.TextInput(attrs={'class': 'form-control'} ),
            'presence': forms.CheckboxInput(),
        }
        labels = {
            'code_pile': 'Code pile',
        }

class QrCodeForm(forms.Form):
    content = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tapez votre message'}),)
    
    
