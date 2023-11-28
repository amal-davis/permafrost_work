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
    path('partner',views.partner,name='partner'),
    path('blast_freezer_and_chiller',views.blast_freezer_and_chiller,name='blast_freezer_and_chiller'),
    path('evaporating_units',views.evaporating_units,name='evaporating_units'),
    path('hermetic_condensing_units',views.hermetic_condensing_units,name='hermetic_condensing_units'),
    path('modular_cold_rooms',views.modular_cold_rooms,name='modular_cold_rooms'),
    path('puff_panels',views.puff_panels,name='puff_panels'),
    path('refrigeneration_products',views.refrigeneration_products,name='refrigeneration_products'),
    path('roofing_panels',views.roofing_panels,name='roofing_panels'),
]