from django.db import models
from django.utils.text import slugify


# Create your models here.
class ProductCategory(models.Model):
    product_category = models.CharField(max_length=128, unique=True, blank=False, null=False)
    parent_category_id = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    slug = models.SlugField(unique=True)
    def __str__(self):
        if self.parent_category_id:
            return f'{self.product_category}, {self.parent_category_id}'
        return f'{self.product_category}'


class Size(models.Model):
    size = models.CharField(max_length=50, unique=True, blank=False, null=False)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.size



class Brand(models.Model):
    brand_name = models.CharField(max_length=128, unique=True, blank=False, null=False)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.brand_name


class Colour(models.Model):
    colour = models.CharField(max_length=64, unique=True, blank=False, null=False)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.colour


class Product(models.Model):
    product_name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    product_description = models.TextField()
    product_category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, related_name='products')
    product_brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='products')
    slug = models.SlugField(editable=True, unique=True)
    # cover = models.ImageField(upload_to='covers/', null=True, blank=True)

    def __str__(self):
        return self.product_name

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.product_name)
    #     super().save(*args, **kwargs)


class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='items')
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.PositiveIntegerField()
    size = models.ForeignKey(Size, blank=True, null=True, on_delete=models.PROTECT, related_name='items')
    colour = models.ForeignKey(Colour, blank=True, null=True, on_delete=models.PROTECT, related_name='items')
    date_of_addition = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)



    class Meta:
        ordering = ('-date_of_addition',)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(f"{self.product.product_name}-{self.colour}-{self.size}")
    #
    #     super(Item, self).save(*args, **kwargs)


