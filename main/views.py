from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Listing
from .forms import ListingForm
from users.forms import LocationForm
import logging
from .filters import ListingFilters

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
    listing_filter = ListingFilters(request.GET, queryset=listings)
    logging.debug(listings)
    context = {
        # 'listings': listings,
        'listing_filter': listing_filter
    }
    
    return render(request, "pages/cars.html",  context)

@login_required
def list_view(request):
    if request.method == 'POST':
        try:
            listing_form = ListingForm(request.POST, request.FILES)
            location_form = LocationForm(request.POST, )
            if listing_form.is_valid() and location_form.is_valid():
                listing = listing_form.save(commit=False)
                listing_location = location_form.save()
                listing.seller = request.user.profile
                listing.location = listing_location
                listing.save()
                messages.info(
                    request, f'{listing.model} Listing Posted Successfully!')
                return redirect('cars')
            else:
                raise Exception()
        except Exception as e:
            print(e)
            logging.debug(e)
            messages.error(
                request, 'An error occured while posting the listing.')
    elif request.method == 'GET':
        listing_form = ListingForm()
        location_form = LocationForm()
    return render(request, 'views/list.html', {'listing_form': listing_form, 'location_form': location_form, })

@login_required
def listing_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        if listing is None:
            raise Exception
        return render(request, 'views/listing.html', {'listing': listing, })
    except Exception as e:
        messages.error(request, f'Invalid UUID {id} was provided for listing.')
        return redirect('home')
    
@login_required
def edit_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        if listing is None:
            raise Exception
        if request.method == 'POST':
            pass
        else:
            pass 
    except Exception as e:
        messages.error(request, f'An error has occured while trying to edit  the listing.')
        return redirect('home')
        # return render(request, 'views/edit.html', {})
    
    
        