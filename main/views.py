from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main_view(request):
    return render(request, "views/main.html",  {"name": "main"})

def aboutus_view(request):
    return render(request, "views/about-us.html", {"name": "aboutus"})

def contact_view(request):
    return render(request, "views/contact-us.html", {"name": "contact"})