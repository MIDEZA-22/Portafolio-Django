from django.shortcuts import redirect, render
from django.core.mail import EmailMessage 
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required 

# Create your views here.
@login_required(login_url='login') 
def contact(request):

    return render(request, 'contact.html', {
        'title': 'Contacto', 
        'nombre': 'Mijail Denis Zavala Llanco',
    })

@login_required(login_url='login') 
def send_mail(request):

    if request.method=="POST":

        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']

        template=render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'message': message,
        })

        email=EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['mideza1993@gmail.com']
        )

        email.fail_silently=False 

        email.send() 

        messages.success(request, 'Tu mensaje se ha enviado correctamente. Muchas gracias por contactarme.')

        return redirect('contact')