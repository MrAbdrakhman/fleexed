
from django.contrib import admin
from .models import Product, Price


admin.site.register(Product)

# Register your models here.


class PriceAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price")


admin.site.register(Price, PriceAdmin)