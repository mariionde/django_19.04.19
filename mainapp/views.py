from django.shortcuts import render
from .models import Product, ProductCategory


def main(request):
    context = {'user': {'name': 'иван'}, 'array': [1, 2, 3, 4, 5]}
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    # Product.objects.filter(category=pk)
    context = {'products': Product.objects.all()}
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    return render(request, 'mainapp/contacts.html')


def common(request):
    return render(request, 'common/index.html')
