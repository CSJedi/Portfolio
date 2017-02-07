from django.shortcuts import render
from django.utils import timezone
from .models import Photo, Price, Contact, About

def photo_list(request):
    photos = Photo.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'portfolio/photo_list.html', {'photos': photos})

def price_list(request):
    prices = Price.objects.order_by('count')
    return render(request, 'portfolio/price_list.html',{'prices': prices})

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'portfolio/contact_list.html', {'contacts':contacts})

def about(request):
    about = About.objects.first()
    return render(request, 'portfolio/about.html', {'about': about})
