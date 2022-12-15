from rest_framework import serializers
from .models import *
from rest_framework import viewsets

class TypeSerializer(serializers.ModelSerializer):
   class Meta:
       model = Type
       fields= '__all__'


class ArticleSerializer(serializers.ModelSerializer):
   class Meta:
       model = Article
       fields= '__all__'



class TypeViewSet(viewsets.ModelViewSet):
   queryset = Type.objects.all()
   serializer_class = TypeSerializer


class ArticleViewSet(viewsets.ModelViewSet):
   queryset = Article.objects.all()
   serializer_class = ArticleSerializer