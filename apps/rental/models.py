from django.db import models
from apps.category.models import Category
from django.urls import reverse

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    size = models.DecimalField(max_digits=8, decimal_places=2)
    unit = models.CharField(max_length=200, unique=False)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=800, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    product_image = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name