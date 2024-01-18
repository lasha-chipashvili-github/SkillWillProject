from django.contrib import admin


from .models import Basket

# Register your models here.
class BasketAdmin(admin.ModelAdmin):
    fields = ('owner', 'item', 'amount', 'total_price', 'is_active')
    list_display = ('id', 'owner', 'item', 'amount', 'total_price', 'date_modified', 'is_active')
    list_display_links = ('id', 'owner',)
    readonly_fields = ('total_price',)

admin.site.register(Basket, BasketAdmin)

