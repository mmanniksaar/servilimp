from django.db import models

class Client(models.Model):
    client_name = models.CharField(max_length=50)
    client_slug = models.SlugField(max_length=200, unique=True)
    client_image = models.ImageField(upload_to='client_pictures')

def get_url(self):
    return reverse('client_name', args=[self.slug])

    def __str__(self):
        return self.client_name