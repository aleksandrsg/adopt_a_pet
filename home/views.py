from django.shortcuts import render

# Create your views here.

def index(request):

    """This view return a home page"""

    return render(request, 'home/index.html')