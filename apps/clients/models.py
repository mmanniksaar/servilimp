from django.db import models
from django.urls import reverse


class Client(models.Model):
    client_name = models.CharField(max_length=50)
    client_slug = models.SlugField(max_length=200, unique=True)
    client_logo = models.ImageField(upload_to='client_pictures')
    client_image = models.ImageField(upload_to='client_pictures')
    modified_date = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return reverse('client_name', args=[self.client_slug])

    def __str__(self):
        return self.client_name