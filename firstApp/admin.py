from django.contrib import admin
from .models import *
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import User
# admin.site.register(User, UserAdmin)
admin.site.register(Article)
admin.site.register(Type)
admin.site.register(Gouvernorat)
admin.site.register(Commande)

# Register your models here.
