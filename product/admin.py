from django.contrib import admin
from .models import Product

# Register your models here.
class ProductModelAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["id", "name", "description", "price"]

admin.site.register(Product, ProductModelAdmin)
