from  appAcercaDe.models import Category_CV

def get_Category(request):
    categories=Category_CV.objects.order_by('order').values_list('id', 'name')

    return {
        'categories': categories,
    }