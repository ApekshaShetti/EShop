from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=20)
    
    @staticmethod
    def get_all_categories():  # function to get all the categories
        return Category.objects.all()
    
    def __str__(self):
        return self.category # in products table category column the value of category will be shown  