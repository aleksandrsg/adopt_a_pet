from django.shortcuts import render
from .models import Pet

# Create your views here.

def pets(request):

    """This view return page this all pets on it"""
    pets = Pet.objects.all()
    context = {
        'pets' : pets,
    }

    return render(request, 'pets/pets.html', context)