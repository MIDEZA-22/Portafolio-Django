from  appAcercaDe.models import Category_CV

def get_Category(request):
    categories=Category_CV.objects.values_list('id', 'name')

    return {
        'categories': categories,
    }