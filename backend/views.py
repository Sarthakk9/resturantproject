from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from frontend.models import About, Blog, Chef, Contact, MenuItem, Reservation
from .forms import AboutForm, BlogForm, ChefForm, ContactForm, MenuItemForm, ReservationForm, SignUpForm, LoginForm


# === General Pages ===

def index(request):
    return render(request, 'backend/index.html')

def dashboard(request):
    return render(request, 'backend/dashboard.html')

def buttons(request):
    return render(request, 'backend/buttons.html')

def typography(request):
    return render(request, 'backend/typography.html')

def elements(request):
    return render(request, 'backend/elements.html')

def charts(request):
    return render(request, 'backend/charts.html')

def signin(request):
    return render(request, 'backend/signin.html')

def signup(request):
    return render(request, 'backend/signup.html')

def error_404(request):
    return render(request, 'backend/404.html')

def blank(request):
    return render(request, 'backend/blank.html')


# === Authentication ===

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('backend:dashboard')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('backend:login')


# === Menu Management ===

def menu_list(request):
    items = MenuItem.objects.all()
    return render(request, 'backend/menu.html', {'menu_items': items})

def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('backend:menu_list')
    else:
        form = MenuItemForm()
    return render(request, 'backend/menu_form.html', {'form': form, 'title': 'Add Menu Item'})

def edit_menu_item(request, id):
    item = get_object_or_404(MenuItem, id=id)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('backend:menu_list')
    else:
        form = MenuItemForm(instance=item)
    return render(request, 'backend/menu_form.html', {'form': form, 'title': 'Edit Menu Item'})

def delete_menu_item(request, id):
    item = get_object_or_404(MenuItem, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('backend:menu_list')
    return render(request, 'backend/delete.html', {'item': item})






# List
def blog_list(request):
    blogs = Blog.objects.all().order_by('-published_date')
    return render(request, 'backend/blog_li.html', {'blogs': blogs})

# Add
def blog_add(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('backend:blog_list')
    else:
        form = BlogForm()
    return render(request, 'backend/blog_form.html', {'form': form, 'title': 'Add Blog'})

# Edit
def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('backend:blog_list')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'backend/blog_form.html', {'form': form, 'title': 'Edit Blog'})

# Delete
def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        blog.delete()
        return redirect('backend:blog_list')
    return render(request, 'backend/blog_confirm_delete.html', {'blog': blog})


# === About Section Management ===

def about_list(request):
    abouts = About.objects.all()
    return render(request, 'backend/about_list.html', {'abouts': abouts})

# Add new About
def about_add(request):
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('backend:about_list')
    else:
        form = AboutForm()
    return render(request, 'backend/about_list.html', {
        'form': form,
        'title': 'Add New About'
    })

# Edit existing About
def about_edit(request, pk):
    about = get_object_or_404(About, pk=pk)
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            form.save()
            return redirect('backend:about_list')
    else:
        form = AboutForm(instance=about)
    return render(request, 'backend/about_form.html', {
        'form': form,
        'title': 'Edit About'
    })

# Delete About
def about_delete(request, pk):
    about = get_object_or_404(About, pk=pk)
    about.delete()
    return redirect('backend:about_list')

# === Chef Management ===

def chef_list(request):
    chefs = Chef.objects.all()
    return render(request, 'backend/chef_list.html', {'chefs': chefs})

def add_chef(request):
    if request.method == 'POST':
        form = ChefForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('backend:chef_list')
    else:
        form = ChefForm()
    return render(request, 'backend/chef_form.html', {'form': form, 'title': 'Add Chef'})

def edit_chef(request, pk):
    chef = get_object_or_404(Chef, pk=pk)
    if request.method == 'POST':
        form = ChefForm(request.POST, request.FILES, instance=chef)
        if form.is_valid():
            form.save()
            return redirect('backend:chef_list')
    else:
        form = ChefForm(instance=chef)
    return render(request, 'backend/chef_form.html', {'form': form, 'title': 'Edit Chef'})

def delete_chef(request, pk):
    chef = get_object_or_404(Chef, pk=pk)
    if request.method == 'POST':
        chef.delete()
        return redirect('backend:chef_list')
    return render(request, 'backend/chef_delete.html', {'chef': chef})

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'backend/reservation_list.html', {'reservations': reservations})

def add_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('backend:reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'backend/add_reservation.html', {'form': form})

def edit_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('backend:reservation_list')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'backend/edit_reservation.html', {'form': form})

def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        reservation.delete()
        return redirect('backend:reservation_list')
    return render(request, 'backend/delete_reservation.html', {'reservation': reservation})



def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'backend/contact_list.html', {'contacts': contacts})

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('backend:contact_list')
    else:
        form = ContactForm()
    return render(request, 'backend/add_contact.html', {'form': form})

def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('backend:contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'backend/edit_contact.html', {'form': form})

def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('backend:contact_list')
    return render(request, 'backend/delete_contact.html', {'contact': contact})


# LOGIN
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('backend:index')  # your dashboard
    else:
        form = AuthenticationForm()
    return render(request, 'backend/login.html', {'form': form})

# SIGNUP
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('backend:login')
    else:
        form = SignUpForm()
    return render(request, 'backend/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('backend:dashboard')
    else:
        form = LoginForm()
    return render(request, 'backend/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('backend:login')

@login_required
def dashboard(request):
    return render(request, 'backend/dashboard.html')



def create_reservation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')

        Reservation.objects.create(
            name=name,
            email=email,
            phone=phone,
            date=date,
            time=time,
            guests=guests
        )

       
        return redirect('backend:reservation_success')
    
    return render(request, 'frontend/reservation.html')


def reservation_success(request):
    
    return render(request, "frontend/success.html")
