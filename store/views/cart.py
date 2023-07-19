from django.views import View
from django.shortcuts import render,redirect
from store.models.customer import Customer # importing this to get the data of all customer which is present in models->customer
from django.contrib.auth.hashers import make_password, check_password # for password hashing in admin panel
from store.models.product import Product
# Cart page
class Cart(View):
    def get(self,request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        return render(request,'cart.html',{'products':products})
