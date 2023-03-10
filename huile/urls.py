"""huile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import index,page,SignUpView,login
from django.views.generic.base import TemplateView
from firstApp.models import *
from django.contrib.auth import views
from firstApp import views as users_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls, name='admin') ,
    # path('salut/',index),
    path('html/', page),
    # path('',TemplateView.as_view(template_name='index.html'),name="home"),
    path('', index ,name='home'),

    path('app/', include('firstApp.urls')),
    # path('signup/', SignUpView.as_view() , name='signup' ),
    path('accounts', include('django.contrib.auth.urls')),
    path(
        'login/',
         views.LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=UserLoginForm
            ),
        name='login'
    ),
    path('signup/',users_views.register, name='signup'),

    #    path(
    #     'signup/',
    #     TemplateView.as_view(
    #         template_name="registration/signup.html",
    #         registrationForm=RegisterForm
    #         ),
    #     name='signup'
# ), 

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
