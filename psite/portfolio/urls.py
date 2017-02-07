from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.photo_list, name='photo_list'),
    url(r'^prices$', views.price_list, name="prices"),
    url(r'^contacts$', views.contacts, name="contacts"),
    url(r'^about$', views.about, name="about"),
]