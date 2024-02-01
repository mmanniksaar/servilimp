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
        'name': 'name',
        'description': 'descripiton',
        'image': 'get_meta_image',
        'modified_date': 'modified_date',
    }
    
    def get_meta_image(self):
        if self.image:
            return self.image.url