from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Listing
from .forms import ListingForm
from users.forms import LocationForm
import logging

def main_view(request):
    return render(request, "views/main.html",  {"name": "main"})

def aboutus_view(request):
    return render(request, "views/about-us.html", {"name": "aboutus"})

def contact_view(request):
    return render(request, "views/contact-us.html", {"name": "contact"})

def products_view(request):
    return render(request, "pages/products.html", {"name": "products"})




# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG)
@login_required
def home_view(request):
    # listings = Listing.objects.all()
    # logging.debug(listings)
    # context = {
    #     'listings': listings,
    # }
    return render (request, "pages/home.html")

@login_required
def car_views(request):
    listings = Listing.objects.all()
    logging.debug(listings)
    context = {
        'listings': listings,
    }
    
    return render(request, "pages/cars.html",  context)

@login_required
def list_view(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        listing_form = ListingForm()
        location_form = LocationForm()
    return render (request, "views/list.html", {'listing_form': listing_form, 'location_form': location_form,})
    
        