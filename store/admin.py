from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order


class AdminProduct(admin.ModelAdmin):   # to view product table in admin panel
    list_display = ['name','price','category']

class AdminCategory(admin.ModelAdmin): # to view category table in admin panel
    list_display = ['category']

# Register your models here.
admin.site.register(Product,AdminProduct) # in admin panel need to see table view of product table
admin.site.register(Category,AdminCategory) # in admin panel need to see table view of category table
admin.site.register(Customer) # in admin panel need to see table view of customer table
admin.site.register(Order)