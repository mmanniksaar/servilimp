from django.contrib import admin
from apps.carts.models import Cart, CartItem

class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'add_date')

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active',)

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)