
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from .forms import UserForm, ProfileForm, LocationForm
from django.views import View
from main.models import Listing, LikedListing
from django.utils.decorators import method_decorator

def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            # print(user)
            if user is not None:
                login(request,user)
                messages.success(
                    request, f'You are now logged as {username}.')
                return redirect('home')
                # return
            else:
                messages.error(request, f'An error unable to login')

        else:
            messages.error(request, f'An error unable to login')

    elif request.method == 'GET':
        login_form = AuthenticationForm()
    return render(request, "views/login.html", {"login_form": login_form})

# function base approac of rendering views
# def register_view(request):
#     register_form = UserCreationForm()
#     return render (request, 'views/register.html', {'register_form' : register_form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('main')

# Class based approach of rendering views 
class RegisterView(View):
    def get(self, request):
        register_form = UserCreationForm()
        return render(request,'views/register.html', {'register_form' : register_form})
    
    def post(self, request):
        register_form = UserCreationForm(data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            user.refresh_from_db()
            # password = register_form.cleaned_data.get('password')
            # user = authenticate(username=user.username, password=password)
            login(request, user)
            messages.success(request, f'user {user.username} registered succesfully..')
            return redirect('home')
        else:
             messages.error(request, f'An error unable to register')
             return render(request,'views/register.html', {'register_form' : register_form})
     
@method_decorator(login_required, name='dispatch')     
class ProfileView(View):
    
    def get(self, request):
        user_listings = Listing.objects.filter(seller=request.user.profile)
        username = Listing(seller=request.user.profile)
        user_liked_listings = LikedListing.objects.filter(profile=request.user.profile).all()
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        location_form = LocationForm(instance=request.user.profile.location)
        return render (request, 'views/profile.html', {
            'user_form': user_form, 
            'profile_form': profile_form, 
            'location_form': location_form,
            'user_listings': user_listings,
            'user_liked_listings': user_liked_listings,
            'username' : username,
            })
    def post(self, request):
        user_listings = Listing.objects.filter(seller=request.user.profile)
        user_liked_listings = LikedListing.objects.filter(profile=request.user.profile).all()
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        location_form = LocationForm(request.POST, instance=request.user.profile.location)
        if user_form.is_valid() and profile_form.is_valid() and location_form.is_valid():
            user_form.save()
            profile_form.save()
            location_form.save()
            messages.success(request, 'Profile Updated  Successfully!')
        else:
            messages.error(request, 'Error Updating Profile ')
        return render (request, 'views/profile.html', {
            'user_form': user_form, 
            'profile_form': profile_form,
            'location_form': location_form,
            'user_listings': user_listings,
            'user_liked_listings': user_liked_listings,
            })
    
    

