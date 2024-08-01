from django.db import models
from django.urls import reverse

from datetime import date

class Gallery(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    gallery_image = models.ImageField(upload_to='gallery_pictures')

    def get_url(self):
        return reverse('description', args=[self.slug])


    def __str__(self):
        return self.description