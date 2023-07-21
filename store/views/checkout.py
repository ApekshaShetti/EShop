from django.views import View
from django.shortcuts import render,redirect
from store.models.customer import Customer # importing this to get the data of all customer which is present in models->customer
from django.contrib.auth.hashers import make_password, check_password # for password hashing in admin panel
from store.models.product import Product
from store.models.orders import Order

# Cart page
class Checkout(View):
    def post(self,request):
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))

        for product in products:
            order = Order(customer = Customer(id = customer), product = product, price = product.price, quantity = cart.get(str(product.id)),
                          address = address,pincode = pincode, phone=phone)
            
            order.placeOrder()


        request.session['cart'] = {}   # empty cart after place order
        
        return redirect('cart')

