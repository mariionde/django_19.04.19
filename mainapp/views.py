from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from basketapp.models import BasketSlot


def main(request):
    return render(request, 'mainapp/index.html')


def products(request, pk=None):
    if pk or pk == 0:
        product_objects = Product.objects.all()
        if pk:
            get_object_or_404(ProductCategory, pk=pk)
            product_objects = Product.objects.filter(category=pk)
        context = {
            'categories': ProductCategory.objects.all(),
            'products': product_objects,
        }
        return render(request, 'mainapp/products.html', context)
    else:
        hot_product = Product.objects.filter(is_hot=True).first()
        context = {
            'categories': ProductCategory.objects.all(),
            'hot_product': hot_product,
        }
        return render(request, 'mainapp/hot_product.html', context)


def contacts(request):
    return render(request, 'mainapp/contacts.html')


def common(request):
    return render(request, 'common/index.html')
