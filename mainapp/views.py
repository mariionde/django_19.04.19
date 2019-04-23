from django.shortcuts import render


def main(request):
    context = {'user': {'name': 'иван'}, 'array': [1, 2, 3, 4, 5]}
    return render(request, 'mainapp/index.html', context)


def products(request):
    return render(request, 'mainapp/products.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')


def common(request):
    return render(request, 'common/index.html')
