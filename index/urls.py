from django.urls import path

from . import views

app_name = 'index'

urlpatterns = [
    path('', views.index, name='home'),
    path('data/', views.data, name='data')
]