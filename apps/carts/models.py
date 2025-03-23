from django.db import models
from apps.accounts.models import Account
from apps.rental.models import Product


class Cart(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)  # Lisatud kasutaja väli
    cart_id = models.CharField(max_length=250, blank=True, unique=True)  # Unikaalne sessiooni-põhine ostukorvi ID
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart: {self.user.username if self.user else self.cart_id}"


class CartItem(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)  # Seos kasutajaga (sisselogitud)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)  # Seos ostukorviga (anonüümne)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.product_name} ({'User' if self.user else 'Cart'})"

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=(
                    models.Q(user__isnull=False) | models.Q(cart__isnull=False)
                ),
                name="cartitem_user_or_cart_must_exist"
            ),
            models.UniqueConstraint(
                fields=["product", "user"],
                name="unique_cartitem_per_user",
                condition=models.Q(user__isnull=False)
            ),
            models.UniqueConstraint(
                fields=["product", "cart"],
                name="unique_cartitem_per_cart",
                condition=models.Q(cart__isnull=False)
            )
        ]
