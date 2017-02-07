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
    description = models.TextField()
    count = models.IntegerField()
    currency = models.CharField(max_length=10)


    '''def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title'''