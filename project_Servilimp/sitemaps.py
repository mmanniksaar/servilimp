from django.contrib import sitemaps
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ["home", "about", "clients", "gallery", "rental", "contact", "cleaning"]

    def location(self, item):
        return reverse(item)