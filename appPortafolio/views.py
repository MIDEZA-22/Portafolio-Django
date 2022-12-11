from django.shortcuts import render
from . models import *
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required 

# Create your views here.
@login_required(login_url='login')
def briefcase(request):

    data_briefcase=Briefcase.objects.filter(public=True).order_by('-order').all()

    paginator=Paginator(data_briefcase, 3)
    page=request.GET.get('page') 
    page_articles=paginator.get_page(page)

    return render(request, 'briefcase.html', {
        'title': 'Portafolio',
        'data_briefcase': page_articles,
    })