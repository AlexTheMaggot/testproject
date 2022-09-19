from django.contrib.auth import authenticate
from django.contrib.auth import logout as logout_view
from django.contrib.auth import login as login_view
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect


def index(request):
    if request.user.is_authenticated:
        template = 'mainapp/index.html'
        return render(request, template)
    else:
        return redirect('mainapp:login', permanent=True)


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
