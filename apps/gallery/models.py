from django.db import models
from django.urls import reverse
from meta.models import ModelMeta

from datetime import date

class Gallery(ModelMeta, models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    gallery_image = models.ImageField(upload_to='gallery_pictures')
    modified_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('description', args=[self.slug])


    def __str__(self):
        return self.description
    
    _metadata = {
        'title': 'name',
        'description': 'descripiton',
        'image': 'get_meta_image',
    }
    
    def get_meta_image(self):
        if self.gallery_image:
            return self.gallery_image.url