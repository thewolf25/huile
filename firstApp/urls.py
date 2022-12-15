from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework import routers
from .api_class import *

router = routers.DefaultRouter()
router.register(r'articles',ArticleViewSet)
router.register(r'typies', TypeViewSet)

urlpatterns = [
    path('', index),
    path('page/',page),
    path('A1', article1, name="Article1"),
    path('A2', article2, name="produits"),
    path('A3', article3, name="ajouterProduit"),
    path('<int:id>/',getArticleById,name="singleArticle"),
    path('api/', include(router.urls)),
    path('code', getUniqueHash, name="code"),
    path('qrcode', getQrCode, name="getQrcode"),
    path('ajoutCommande' , ajoutCommande , name="ajoutCommande"),
    path('ajoutFournisseur' , ajoutFournisseur , name="ajoutFournisseur"),
    path('commandes', CommandeList, name="commandeList"),
    path('commande/<str:id>',SingleCommande,name="singleCommande"),
    path('degustateur/<str:code>' , AddDegustateurNotes , name="addDegustateurNotes"),
    path('createDegustateurNote',createDegustateurNote, name="createDegustateurNote")
]
