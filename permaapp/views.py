import select
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string

from .models import *
import random
import string

# Create your views here.

def index_page(request):
    return render(request,'index.html')


def about_us(request):
    return render(request,'about-us.html')


def services(request):
    return render(request, 'services.html')


def contact_us(request):
    return render(request,'contact-us.html')


def gallery(request):
    return render(request,'gallery.html')


def partner(request):
    return render(request,'partner.html')


def blast_freezer_and_chiller(request):
    return render(request,'Blast_freezer_and_chiller.html')


def evaporating_units(request):
    return render(request,'Evaporating_Units.html')


def hermetic_condensing_units(request):
    return render(request,'Hermetic_Condensing_units.html')


def modular_cold_rooms(request):
    return render(request,'Modular_Cold_Rooms.html')


def puff_panels(request):
    return render(request,'Puff_Panels.html')


def refrigeneration_products(request):
    return render(request,'Refrigeration_Products.html')


def roofing_panels(request):
    return render(request,'Roofing_Panels.html')