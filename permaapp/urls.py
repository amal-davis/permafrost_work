from django.urls import path
from  permaapp import views
from  django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('',views.index_page,name='index_page'),
    path('about_us',views.about_us,name='about_us'),
    path('services',views.services,name='services'),
    path('contact_us',views.contact_us,name='contact_us'),
    path('gallery',views.gallery,name='gallery'),
]