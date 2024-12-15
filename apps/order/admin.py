from django.contrib import admin
from .models import Cart, CartItem
from django.utils.html import format_html


admin.site.register(CartItem)
admin.site.register(Cart)