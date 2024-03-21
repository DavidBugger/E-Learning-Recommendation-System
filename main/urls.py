from django.urls import path
from .views import main_view,aboutus_view,contact_view, home_view

urlpatterns = [
    path('', main_view, name = 'main'),
    path('about-us/', aboutus_view, name = 'about'),
    path('contact-us/', contact_view, name = 'contact'),
    path('home/', home_view, name = 'home')

]
