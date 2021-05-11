from django.shortcuts import render
from .models import Comment
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime


def index(request):
    return render(request, 'website/index.html', {})


def about(request):
    return render(request, 'website/about.html', {})


def services(request):
    return render(request, 'website/services.html', {})







# Create your views here.
