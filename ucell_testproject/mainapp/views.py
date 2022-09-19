from django.contrib.auth import authenticate
from django.contrib.auth import logout as logout_view
from django.contrib.auth import login as login_view
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from .models import Product


def index(request):
    if request.method == 'GET':
        if 'search' in request.GET:
            products = Product.objects.filter(name__contains=request.GET['search'])
        else:
            products = Product.objects.all()
        if request.user.is_authenticated:
            template = 'mainapp/index.html'
            context = {
                'products': products
            }
            return render(request, template, context)
        else:
            return redirect('mainapp:login', permanent=True)
    elif request.method == 'POST':
        product = Product.objects.get(id=request.POST['id'])
        product.quantity = request.POST['quantity']
        product.save()
        return redirect('mainapp:index', permanent=True)
    else:
        return HttpResponseForbidden()


def login(request):
    if request.method == 'GET':
        template = 'mainapp/login.html'
        if 'auth' in request.GET:
            context = {'wrong_auth': request.GET['auth']}
            return render(request, template, context)
        else:
            return render(request, template)
    elif request.method == 'POST':
        try:
            User.objects.get(username=request.POST['username'])
        except ObjectDoesNotExist:
            return redirect('/login/?auth=wrong_login', permanent=True, )
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login_view(request, user)
            return redirect('mainapp:index', permanent=True)
        else:
            return redirect('/login/?auth=wrong_password', permanent=True,)
    else:
        return HttpResponseForbidden()
    pass


def logout(request):
    logout_view(request)
    return redirect('mainapp:login')
