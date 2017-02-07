from django.db import models
from django import forms
from django.utils import timezone

class ImageUpload(forms.Form):
    image = forms.ImageField()

class Photo(models.Model):
    model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no_image_300x300.jpg')
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    description = models.TextField()
    published_date = models.DateTimeField( blank=True, null=True)
    
class Price(models.Model):
    count = models.IntegerField()
    currency = models.CharField(max_length=10)
    description = models.TextField()

class Contact(models.Model):
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

class About(models.Model):
    title =  models.CharField(max_length=200)
    description = models.TextField()