from django.shortcuts import render
from .models import MenuItem

def index(request):
    return render(request, 'menu/index.html', context={'items' : MenuItem.objects.all()})
