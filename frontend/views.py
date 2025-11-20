from django.shortcuts import render
from . models import MenuItem, About, Chef, Blog, Reservation 

def index(request):
    return render(request, 'frontend/index.html')

def menu(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'frontend/menu.html', {'menu_items': menu_items})

def about(request):
    about_items = About.objects.all()
    return render(request, 'frontend/about.html', {'about_items': about_items})

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'frontend/blog.html', {'blogs': blogs})

def chef(request):
    chefs = Chef.objects.all()
    return render(request, 'frontend/chef.html', {'chefs': chefs})

def contact(request):
    return render(request, 'frontend/contact.html')

def reservation(request):
    return render(request, 'frontend/reservation.html')