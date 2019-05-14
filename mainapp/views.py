from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from basketapp.models import BasketSlot


def main(request):
    return render(request, 'mainapp/index.html')


def products(request, pk=None):
    basket = []
    if request.user.is_authenticated:
        basket = BasketSlot.objects.filter(user=request.user)

    total_quantity = sum(list(map(lambda basket_slot: basket_slot.quantity, basket)))

    if pk:
        get_object_or_404(ProductCategory, pk=pk)
        product_objects = Product.objects.filter(category=pk)
    else:
        product_objects = Product.objects.all()
    context = {
        'categories': ProductCategory.objects.all(),
        'products': product_objects,
        'basket_quantity': total_quantity,
    }
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    return render(request, 'mainapp/contacts.html')


def common(request):
    return render(request, 'common/index.html')
