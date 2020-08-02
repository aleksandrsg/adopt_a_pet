from django.urls import path
from . import views

urlpatterns = [
    path('', views.pets, name='pets'),
    path('<name>/', views.pet_desc, name='pet_desc'),
    path('gallery', views.gallery, name='gallery'),
]