from django.shortcuts import render


def index(request):
    return render(request, 'website/index.html', {})


def generic(request):
    return render(request, 'website/about.html', {})


def elements(request):
    return render(request, 'website/elements.html', {})

# Create your views here.
