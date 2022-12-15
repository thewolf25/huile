from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.urls import reverse
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import QrCodeForm,RegisterForm,FournisseurForm,CommandeForm
from .filters import ListingFilter ,CommandeFiler
import random
import os
from django.core.paginator import Paginator
import uuid
from django.http import JsonResponse
import qrcode
import csv
from django.conf import settings
from django.contrib.auth.decorators import login_required



def index(request):
    return HttpResponse("<h1>Hello app2 </h2>")

def page(request):
    return render( request,'firstApp/index.html',{'date': datetime.now()})

def article1(request):
    return render(request ,'firstApp/article 1.html')


@login_required(login_url='login') 
def getQrCode(request):
    if(request.POST):
        form = QrCodeForm(request.POST)
        if(form.is_valid()):
            print(form.data['content'])
            a = qrcode.make(form.data['content'])
            a.save(settings.MEDIA_ROOT/'MyQRCode1.png')
            url = 'MyQRCode1.png'
            return render(request,'firstApp/qrcodeViewer.html'  , {
                'url' : url
            })
    form = QrCodeForm()
    return render(request, 'firstApp/qrcodeViewer.html',{
        'qrForm': form
    })


def article3(request):
    articleForm = ArticleForm()
    if(request.method == 'POST'):
        articleForm = ArticleForm(request.POST)
        if articleForm.is_valid():
           articleForm.save()
           articleForm= ArticleForm()
           return render(request , 'firstApp/article 3.html',
                        {
                      'articleForm': articleForm,
                      'message' : "Article ajouter avec succées !!!!"

                        })
    return render(request , 'firstApp/article 3.html', 
                  {
                      'articleForm': articleForm
                  })

def getArticleById(request,id):
    result = Article.objects.get(pk=id)
    context = {'article' : result}
    return render(request, 'firstApp/article 1.html', context)

def getUniqueHash(request):
    return JsonResponse({'code' : uuid.uuid4().hex[:10]})

def register(request):
    if request.method == 'GET':
        form  = RegisterForm()
        context = {'form': form}
        return render(request, 'registration/signup.html', context)
    if request.method == 'POST':
        form  = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('home')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'registration/signup.html', context)

    return render(request, 'registration/signup.html', {})

def ajoutFournisseur(request):
    commandeForm = CommandeForm()
    if(request.method == 'POST'):
        fournisseurForm = FournisseurForm(request.POST)
        if fournisseurForm.is_valid():
           fournisseurForm.save()
           return HttpResponseRedirect(reverse("ajoutCommande"))
    fournisseurs= Fournisseur.objects.all()
    fournisseurForm = FournisseurForm()

    return render(request , 'firstApp/commande.html', 
                  {
                      'fournisseur': fournisseurs,
                      'fournisseurForm': fournisseurForm,
                      'commandeForm': commandeForm
                  })


def ajoutCommande(request):
    fournisseurForm = FournisseurForm()
    if(request.method == 'POST'):
        commandeForm = CommandeForm(request.POST)
        if commandeForm.is_valid():
           commandeForm.save()
           return HttpResponseRedirect(reverse("ajoutCommande"))

    fournisseurs= Fournisseur.objects.all()
    commandeForm = CommandeForm()

    return render(request , 'firstApp/commande.html', 
                  {
                      'fournisseur': fournisseurs,
                      'fournisseurForm': fournisseurForm,
                      'commandeForm': commandeForm
                  })
    
    
def createGouvernorat():

    with open('state.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} works in the {row[1]} department, .')
                line_count += 1
                gouvene = Gouvernorat(libelle=row[1])
                gouvene.save()
        print(f'Processed {line_count} lines.')

def article2(request):        
    articleList = Article.objects.all()
    articleFilter= ListingFilter(request.GET, queryset=articleList)
    articles= Paginator(articleFilter.qs, 3)
    page_number = request.GET.get('page')
    page_obj = articles.get_page(page_number)
    for i in articleFilter.form.fields:
        articleFilter.form.fields[i].widget.attrs = {'class' : 'form-control'}
    return render(request ,'firstApp/article 2.html',
                  {
                      'articleList': articleFilter ,
                      'articles': page_obj
                      }
                  )


def CommandeList(request):
    commandes = Commande.objects.all()
    commandeFilter= CommandeFiler(request.GET, queryset=commandes)
    commandeList= Paginator(commandeFilter.qs, 3)
    page_number = request.GET.get('page')
    page_obj = commandeList.get_page(page_number)
    print(User.objects.filter(groups__name='fournisseur'))
    for i in commandeFilter.form.fields:
        commandeFilter.form.fields[i].widget.attrs = {'class' : 'form-control'}
    # return render(request, 'list.html', {'page_obj': page_obj})
    return render(request, 'firstApp/commandeList.html' , {
        # 'commandeList' : commandeList,
        'commandeList': page_obj,
        'commandeFilter': commandeFilter
    })
    
def SingleCommande(request,id):
    result = Commande.objects.get(code=id)
    print("dégustateur Note")
    print(result.degustateursnotes_set)
    if(request.method == 'POST'):
        note = request.POST.get('note')
        result.note = note
        result.save()
        return HttpResponseRedirect(reverse("singleCommande",kwargs={'id':id}))

    context = {'commande' : result}
    print(result.degustateurs)
    return render(request, 'firstApp/singleCommande.html', context)



def AddDegustateurNotes(request, code): 
    commande = Commande.objects.filter(code=code)

    return render(request,'firstApp/degustateurMarks.html' , {
        'code' : code,
        'commande': commande
    })

def createDegustateurNote(request):
    # print(request.POST)
    code = request.POST.get('code')
    note = request.POST.get('note')
    commande = Commande.objects.filter(code=code).first()
    user = User.objects.get(pk=request.user.id)
    try:
        DegustateursNotes.objects.create(commande=commande,user=user,note=note)
    except:
        degustateurNote = DegustateursNotes.objects.filter(commande=commande,user=user).first()
        degustateurNote.note = note
        degustateurNote.save()
        return HttpResponseRedirect(reverse("singleCommande",kwargs={'id': code}))

    return HttpResponse(user)
    
