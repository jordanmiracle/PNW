from django.shortcuts import get_object_or_404, render


def index(request):
    return render(request, 'website/index.html', {})


def services(request):
    return render(request, 'website/services.html', {})





# Create your views here.
