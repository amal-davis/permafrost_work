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