from django.urls import path
from . import views

urlpatterns = [
    path('', views.pets, name='pets'),
    path('<pet_id>', views.pet_desc, name='pet_desc'),
]
