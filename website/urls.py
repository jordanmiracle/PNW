from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap  # new
from django.contrib.sitemaps.views import sitemap
from .sitemaps import Static_Sitemap, Review_Sitemap
from website.models import Review
from django.views.generic.base import TemplateView  # import TemplateView

sitemaps = {
    'article': Review_Sitemap(),
    'static': Static_Sitemap(),
}

info_dict = {
    'queryset': Review.objects.all(),
}

urlpatterns = [
    path('', views.index, name="index"),
    path('about.html', views.generic, name='about'),
    path('reviews.html', views.elements, name='reviews'),
    path('sitemap.xml', sitemap, {'sitemaps': {'Reviews': GenericSitemap(info_dict, priority=0.6)}},
         name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt", TemplateView.as_view(template_name="website/robots.txt", content_type="text/plain")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
