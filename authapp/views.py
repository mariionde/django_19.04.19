from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.contrib import auth
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from authapp.forms import ShopUserRegisterForm
from django.urls import reverse_lazy
from authapp.models import ShopUser


def register(request):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            user = register_form.save()
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))
    else:
        register_form = ShopUserRegisterForm()

    context = {'title': title, 'form': register_form}

    return render(request, 'authapp/register.html', context)


def login(request):
    title = 'вход'

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))

    context = {'title': title}
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


class EditView(UpdateView):
    model = ShopUser
    template_name = 'authapp/register.html'
    fields = ('username', 'first_name', 'last_name', 'age', 'avatar')
    success_url = reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super(EditView, self).get_context_data(**kwargs)
        context['title'] = 'Изменение пользователя'
        return context
