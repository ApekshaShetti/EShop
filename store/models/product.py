from django.db import models
from .category import Category # connection between product and category
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=255,default='',null=True,blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1) # relation between product and category, if any category is deleted the product from that category will also be deleted

    @staticmethod
    def get_all_products():  # function to get all the products
        return Product.objects.all()
    
    @staticmethod
    def get_all_products_by_category_id(category_id):  # function to get the products with same category id 
        if category_id:
            # if category id is given the show only those products with that category id 
            return Product.objects.filter(category = category_id)
        else:
            # if category id is not given then show all products 
            return Product.get_all_products()