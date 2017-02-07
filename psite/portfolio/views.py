from django.shortcuts import render
from django.utils import timezone
from .models import Photo
from .models import Price

def photo_list(request):
    photos = Photo.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'portfolio/photo_list.html', {'photos': photos})

def price_list(request):
    prices = Price.objects.order_by('count')
    return render(request, 'portfolio/price_list.html',{'prices': prices})

def contacts(request):
    return render(request, 'portfolio/contacts.html', {})

def about(request):
    return render(request, 'portfolio/about.html', {})
