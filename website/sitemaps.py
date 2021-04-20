from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Reviews


class Static_Sitemap(Sitemap):

    priority = 1.0
    changefreq = 'yearly'

    def items(self):
        return ['about', 'index', 'elements']

    def location(self, item):
        return reverse(item)


class Review_Sitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Reviews.objects.all()

    def location(self, obj):
        return obj.note_full_path

    def lastmod(self, obj):
        return obj.date_modified