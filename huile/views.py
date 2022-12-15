from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import  UserCreationForm
from firstApp.decorators import *
from django.views.generic.base import TemplateView
from django.contrib.auth import views
from firstApp.models import *

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url= reverse_lazy('login')
    template_name = "registration/signup.html"
    
@redirectByRole  
def index(request):
    return HttpResponse("<h1>Salem si mehdi</h1>")

def page(request):
    context = {'name': 'mehdi' , 'date': datetime.now}
    return render(request, 'index.html',context)
def login(request):
    if(request.user.is_authenticated):
        return redirect('home')
    
    return views.LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=UserLoginForm
            ),