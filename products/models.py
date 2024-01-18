from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class ProductCategory(models.Model):
    product_category = models.CharField(max_length=128, unique=True, blank=False, null=False)
    parent_category_id = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    slug = models.SlugField(max_length=128, unique=True)
    def __str__(self):
        if self.parent_category_id:
            return f'{self.product_category}, {self.parent_category_id}'
        return f'{self.product_category}'


class Size(models.Model):
    size = models.CharField(max_length=50, unique=True, blank=False, null=False)
    slug = models.SlugField(max_length=50, unique=True)
    def __str__(self):
        return self.size



class Brand(models.Model):
    brand_name = models.CharField(max_length=128, unique=True, blank=False, null=False)
    slug = models.SlugField(max_length=128, unique=True)
    def __str__(self):
        return self.brand_name


class Colour(models.Model):
    colour = models.CharField(max_length=64, unique=True, blank=False, null=False)
    slug = models.SlugField(max_length=64, unique=True)
    def __str__(self):
        return self.colour


class Product(models.Model):
    class WhomAssigned(models.IntegerChoices):
        MEN = -1, 'Men'
        WOMEN = 1, 'Women'
        KIDS = 0, 'kids'


    product_name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    product_description = models.TextField()
    product_category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, related_name='products')
    product_brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='products')
    prod_slug = models.SlugField(max_length=255, editable=True, unique=True)
    whom_assigned = models.IntegerField(choices=tuple(map(lambda x: (int(x[0]), x[1]), WhomAssigned.choices)),
                                       default=WhomAssigned.WOMEN, verbose_name="whom assigned")
    special_offer = models.BooleanField(default=False)
    new_arrival = models.BooleanField(default=True)
    prod_price = models.DecimalField(default=0.0, max_digits=7, decimal_places=2)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})


    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.product_name)
    #     super().save(*args, **kwargs)


class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='items')
    itm_slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    stock = models.PositiveIntegerField()
    size = models.ForeignKey(Size, blank=True, null=True, on_delete=models.PROTECT, related_name='items')
    colour = models.ForeignKey(Colour, blank=True, null=True, on_delete=models.PROTECT, related_name='items')
    date_of_addition = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)



    class Meta:
        ordering = ('-date_of_addition',)


    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.product.prod_price

        super(Item, self).save(*args, **kwargs)


    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(f"{self.product.product_name}-{self.colour}-{self.size}")
    #
    #     super(Item, self).save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='images')
    files = models.FileField(upload_to='static/products/', default=None,
                              blank=True, null=True, verbose_name="Images")

# class ItemImage(models.Model):
#     item = models.ForeignKey(Item, on_delete=models.PROTECT)
#     files = models.FileField(upload_to='static/items/', default=None,
#                               blank=True, null=True, verbose_name="Images")
