from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'search_fitur'
urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.searchposts, name='cari'),
    # path('category/<str:kategori>/', views.kategori, name='awal'),
    path('category/', views.kategori, name='awal'),
    path('<int:blog_id>/', views.coba, name='halo'),
    path('coba/', views.coba, name='wow'),
    path('category/<str:kategori>/', views.searchposts2, name="kategori")
   
]