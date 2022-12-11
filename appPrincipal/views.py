from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required 

# Create your views here.
@login_required(login_url='login')
def cover_page(request):

    return render(request, 'cover_page.html', {
        'title': 'Portada',
        'name': 'Mijail Denis Zavala Llanco',
    })

def login_page(request):

    if request.user.is_authenticated: 
        return redirect('cover_page')   
    else:    
        if request.method=='POST':

            username=request.POST.get('username') 
            password=request.POST.get('password') 

            user=authenticate(request, username=username, password=password)
            
            if user is not None:

                login(request, user)

                return redirect('cover_page')

            else:

                messages.warning(request, 'No te has identificado correctamente.')
        
        return render(request, 'users/login.html',{
            'title':'Acceso'
        })

def logout_user(request):

    logout(request) 

    return redirect('login')