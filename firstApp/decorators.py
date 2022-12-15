from django.shortcuts import redirect
from django.http import HttpResponse

def redirectByRole(s):
    def wrapper_func(request,*args,**kwargs):
        if(not request.user.is_authenticated):
            return redirect("login")
        if(request.user.is_superuser):
            return redirect('admin:index')
        group = request.user.groups.all()
        if(len(group) > 0):
            if(group == "customer"):
                return redirect('produits')
            else:
                return redirect('commandeList')
        return redirect('commandeList')
    return wrapper_func
