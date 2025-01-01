from django.db import models
from accounts.models import Account
from store.models import Product

# Create your models here.

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user=models.ForeignKey(Account, on_delete=models.CASCADE ,blank=True, null=True)
    quantity = models.IntegerField(default=0)
    color = models.CharField(max_length=50, blank=True)
    size = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity
    
    
    def __str__(self):
        return self.product.product_name


