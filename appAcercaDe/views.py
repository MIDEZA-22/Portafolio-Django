from django.shortcuts import render
from . models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required 

# Create your views here.
@login_required(login_url='login')
def acercaDe(request):

    return render(request, 'about.html', {
        'title': 'Acerca De',
        'nombre': 'Mijail Denis Zavala Llanco',
    })

@login_required(login_url='login')
def education(request, name_category):

    name_category=Category_CV.objects.get(name=name_category)
    data_education=Education.objects.select_related('category').filter(public=True).order_by('-order').all()
    
    paginator=Paginator(data_education, 3) 
    page=request.GET.get('page')
    page_articles=paginator.get_page(page)

    return render(request, 'categories/educacion.html', {
        'name_category': name_category,
        'data_education': page_articles,
    })

@login_required(login_url='login')
def experience(request, name_category):

    name_category=Category_CV.objects.get(name=name_category) 
    data_experience=Experience.objects.select_related('category').filter(public=True).order_by('-order').values_list('entity', 'held_position', 'functions', 'start_date', 'finish_date') 
    
    paginator=Paginator(data_experience, 3)
    page=request.GET.get('page')
    page_articles=paginator.get_page(page)

    return render(request, 'categories/experiencias_laborales.html', {
        'name_category': name_category,
        'data_experience': page_articles,
    })

@login_required(login_url='login') 
def pre_professional_practice(request, name_category):

    name_category=Category_CV.objects.get(name=name_category) 
    data_pre_professional_practice=Pre_Professional_Practice.objects.select_related('category').filter(public=True).order_by('-order').values_list('entity', 'held_position', 'functions', 'start_date', 'finish_date') 
    
    paginator=Paginator(data_pre_professional_practice, 3) 
    page=request.GET.get('page') 
    page_articles=paginator.get_page(page)

    return render(request, 'categories/practica_pre_profesional.html', {
        'name_category': name_category,
        'data_pre_professional_practice': page_articles,
    })

@login_required(login_url='login') 
def volunteering(request, name_category):

    name_category=Category_CV.objects.get(name=name_category) 
    data_volunteering=Volunteering.objects.select_related('category').filter(public=True).order_by('-order').values_list('entity', 'held_position', 'functions', 'start_date', 'finish_date') 
    
    paginator=Paginator(data_volunteering, 3) 
    page=request.GET.get('page')
    page_articles=paginator.get_page(page)

    return render(request, 'categories/voluntariados.html', {
        'name_category': name_category,
        'data_volunteering': page_articles,
    })

@login_required(login_url='login')
def computers_skill(request, name_category):

    name_category=Category_CV.objects.get(name=name_category) 
    data_computers_skill=Computers_Skill.objects.select_related('category').filter(public=True).order_by('-order').values_list('name', 'framework', 'level') 
    
    paginator=Paginator(data_computers_skill, 6) 
    page=request.GET.get('page')
    page_articles=paginator.get_page(page)

    return render(request, 'categories/habilidades_informaticas.html', {
        'name_category': name_category,
        'data_computers_skill': page_articles,
    })

@login_required(login_url='login')
def language(request, name_category):

    name_category=Category_CV.objects.get(name=name_category) 
    data_language=Language.objects.select_related('category').filter(public=True).order_by('-order').values_list('entity','name', 'level') 
    
    paginator=Paginator(data_language, 6)
    page=request.GET.get('page')
    page_articles=paginator.get_page(page)

    return render(request, 'categories/lenguajes.html', {
        'name_category': name_category,
        'data_language': page_articles,
    })

@login_required(login_url='login')
def achievement(request, name_category):

    name_category=Category_CV.objects.get(name=name_category) 
    data_achievement=Achievement.objects.select_related('category').filter(public=True).order_by('-order').all() 
    
    paginator=Paginator(data_achievement, 3)
    page=request.GET.get('page')
    page_articles=paginator.get_page(page)

    return render(request, 'categories/logros.html', {
        'name_category': name_category,
        'data_achievement': page_articles,
    })

@login_required(login_url='login')
def course(request, name_category):

    name_category=Category_CV.objects.get(name=name_category) 
    data_course=Course.objects.select_related('category').filter(public=True).order_by('-order').values_list('entity', 'name', 'start_date', 'finish_date', 'duration')
    
    paginator=Paginator(data_course, 6)
    page=request.GET.get('page')
    page_articles=paginator.get_page(page)

    return render(request, 'categories/cursos.html', {
        'name_category': name_category,
        'data_course': page_articles,
    })

@login_required(login_url='login')
def congress(request, name_category):

    name_category=Category_CV.objects.get(name=name_category)
    data_congress=Congress.objects.select_related('category').filter(public=True).order_by('-order').values_list('entity', 'name', 'start_date', 'finish_date', 'duration') 
    
    paginator=Paginator(data_congress, 6) 
    page=request.GET.get('page') 
    page_articles=paginator.get_page(page)

    return render(request, 'categories/congresos.html', {
        'name_category': name_category,
        'data_congress': page_articles,
    })

@login_required(login_url='login')
def training(request, name_category):

    name_category=Category_CV.objects.get(name=name_category)
    data_training=Training.objects.select_related('category').filter(public=True).order_by('-order').values_list('entity', 'name', 'start_date', 'finish_date', 'duration')
    
    paginator=Paginator(data_training, 6) 
    page=request.GET.get('page') 
    page_articles=paginator.get_page(page)

    return render(request, 'categories/capacitaciones.html', {
        'name_category': name_category,
        'data_training': page_articles,
    })

@login_required(login_url='login')
def references(request, name_category):

    name_category=Category_CV.objects.get(name=name_category) 
    data_references=References.objects.select_related('category').filter(public=True).order_by('-order').values_list('name', 'held_position', 'entity', 'phone') 
    
    paginator=Paginator(data_references, 5)
    page=request.GET.get('page') 
    page_articles=paginator.get_page(page)

    return render(request, 'categories/referencias.html', {
        'name_category': name_category,
        'data_references': page_articles,
    })

@login_required(login_url='login')
def other_data(request, name_category):

    name_category=Category_CV.objects.get(name=name_category) 
    data_other_data=Other_Data.objects.select_related('category').filter(public=True).order_by('-order').all()
    
    paginator=Paginator(data_other_data, 3)
    page=request.GET.get('page')
    page_articles=paginator.get_page(page)

    return render(request, 'categories/otros_datos.html', {
        'name_category': name_category,
        'data_other_data': page_articles,
    })