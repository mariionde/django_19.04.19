from django.shortcuts import render
from .models import Product, ProductCategory


def main(request):
    return render(request, 'mainapp/index.html')


def products(request, pk=None):
    # Product.objects.filter(category=pk)
    context = {'products': Product.objects.all()}
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    return render(request, 'mainapp/contacts.html')


def common(request):
    return render(request, 'common/index.html')
