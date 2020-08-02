from django.shortcuts import render, get_object_or_404
from .models import Pet, Category
from django.core.paginator import Paginator

# Create your views here.

def pets(request):

    """This view return page this all pets on it"""
    pets = Pet.objects.all()
    categories = None

    paginator = Paginator(pets, 3)
    page = request.GET.get('page')
    pets = paginator.get_page(page)

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category']
            pets = pets.filter(category__name__in = categories)
            categories = Category.objects.all()
        
    context = {
        'pets' : pets,
        'categories' : categories,
    }

    return render(request, 'pets/pets.html', context)


def pet_desc(request, name):

    """This view return pet description"""
    pet = Pet.objects.get(name=name)
    context = {
        'pet' : pet,
    }

    return render(request, 'pets/pet_desc.html', context)

def gallery(request):

    return render(request, 'pets/gallery.html')
