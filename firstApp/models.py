from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField,UserCreationForm
from django.utils.translation import gettext_lazy as _
import uuid
from django.core.exceptions import ValidationError
from datetime import datetime
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    error_messages = {
        'invalid_login': _(
            "Priére d'  insérer un nom d'utilisateur et un mot de passe correct"
            "les champs peuvent être sensibles à la casse"
        ),
        'inactive': _("Ce compte est inactive"),
    }
    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'hi',
        }
))
    

# class User(AbstractUser):
#     # city= models.CharField(max_length=100)
#     pass

class Type(models.Model):
    libelle= models.CharField(max_length=100,null=False)
    def __str__(self):
        return "%s" % (self.libelle)

State = (
    ('validé', 'Vaidé') , 
    ('en attente', 'En Attente') ,
    ('refusée', 'Refusée')
)


# def uniqueHash():
#     condition = True
#     uniqueCode = uuid.uuid4().hex[:10]
#     while condition:
#         articles = Article.objects.filter(code=uniqueCode)
#         if(len(articles) != 0):
#             condition=False
#     return uniqueCode

def postiveValueValidator(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s La quantité ne doit pas étre négatif'),
            params={'value': value},
        )
class Article(models.Model):
    nom = models.CharField(max_length=100)
    status = models.CharField(max_length=100 ,choices=State)
    qte= models.IntegerField(validators=[postiveValueValidator])
    type= models.ForeignKey(Type,on_delete=models.CASCADE,null=True,unique=False)



class ArticleForm(ModelForm):
    error_css_class = "alert alert-danger"

    class Meta:
        model= Article
        fields= '__all__'
        exclude = ('code',)
        widgets = {
            'qte': forms.NumberInput(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }
        

        
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class' : 'form-control'})
    )
    
class Gouvernorat(models.Model):
    libelle =  models.CharField(max_length=100, blank=False)
    def __str__(self):
        return "%s" % (self.libelle)


class Ville(models.Model):
    libelle =  models.CharField(max_length=100, blank=False)
    gouvernorat =  models.ForeignKey(Gouvernorat,on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.libelle)

    
class Fournisseur(models.Model):
    nom = models.CharField(blank=False,max_length=100)
    contact = models.CharField(null=True, max_length=100)
    telephone = models.CharField(null=True,max_length=100)
    addresse = models.CharField(blank=False,max_length=100)
    gouvernorat =  models.ForeignKey(Gouvernorat,on_delete=models.CASCADE)
    ville =  models.ForeignKey(Ville,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return "%s %s" % (self.nom ,self.gouvernorat.libelle) 

    
class Commande(models.Model):
    code = models.CharField(max_length=100 , unique=True ,default=datetime.now().strftime('%Y%m%d%H%M%S') + str(uuid.uuid4().hex[5]))
    qte= models.IntegerField()
    gouvernorat = models.ForeignKey(Gouvernorat,on_delete=models.CASCADE)
    dateEchantion = models.DateTimeField(auto_created=True, default=datetime.now())
    code_pile = models.CharField(max_length=100)
    fournisseur = models.ForeignKey(Fournisseur,on_delete=models.CASCADE)
    cellage = models.CharField(max_length=100,null=True)
    presence = models.BooleanField(default=False)
    status = models.CharField(max_length=100 ,choices=State,null=True,default=('en attente', 'En Attente'))
    note = models.TextField(null=True)
    degustateurs = models.ManyToManyField(User,through='DegustateursNotes')

class DegustateursNotes(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField(max_length=200)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['commande', 'user'], name='unique_user_commande_combination'
            )
        ]
    def __str__(self):
        return "{}_{}".format(self.user.__str__(), self.commande.__str__())