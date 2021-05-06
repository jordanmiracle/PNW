from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Comment


class Static_Sitemap(Sitemap):
    priority = 1.0
    changefreq = 'yearly'

    def items(self):
        return ['about', 'index', 'elements']

    def location(self, item):
        return reverse(item)
