from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'search_fitur'
urlpatterns = [
  
    path('', views.index, name='index'),
#   hasil dari search home
    path('result/', views.searchposts, name='cari'),

    path('category/', views.kategori, name='awal'),
    path('<int:blog_id>/', views.coba, name='halo'),
#   kalo klik baca selengkapnya di homepage
    path('coba/', views.coba, name='wow'),
    path('category/<str:kategori>/', views.searchposts2, name="kategori"),
    path('register', views.register, name='register'),
]
