from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Listing
# Create your views here.

def main_view(request):
    return render(request, "views/main.html",  {"name": "main"})

def aboutus_view(request):
    return render(request, "views/about-us.html", {"name": "aboutus"})

def contact_view(request):
    return render(request, "views/contact-us.html", {"name": "contact"})

def products_view(request):
    return render(request, "pages/products.html", {"name": "products"})

def car_views(request):
    return render(request, "pages/cars.html", {"name": "cars"})

@login_required
def home_view(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings,
    }
    return render (request, "pages/home.html", context)