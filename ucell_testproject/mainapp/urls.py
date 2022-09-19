from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
