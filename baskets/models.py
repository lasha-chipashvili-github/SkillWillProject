from django.db import models

from accounts.models import CustomUser
from products.models import Item, Product


# Create your models here.

class Basket(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)
    total_price = models.FloatField(default=0.00)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    # def __str__(self):
    #     return f'{self.item} in basket for {self.owner.email}'


    def get_total_price(self):
        self.total_price = self.item.price * self.amount
        return self.total_price

    def save(self):
        self.total_price = self.get_total_price()
        super(Basket, self).save()

class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
