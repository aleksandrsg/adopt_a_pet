from django.shortcuts import render, get_object_or_404
from .models import Pet

# Create your views here.

def pets(request):

    """This view return page this all pets on it"""
    pets = Pet.objects.all()
    context = {
        'pets' : pets,
    }

    return render(request, 'pets/pets.html', context)


def pet_desc(request, pet_id):

    """This view return pet description"""
    pet = get.object_or_404(Pet, pk=pet_id)
    context = {
        'pet' : pet,
    }

    return render(request, 'pets/pet_desc.html', context)