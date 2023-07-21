from django.views import View
from django.shortcuts import render,redirect
from store.models.customer import Customer # importing this to get the data of all customer which is present in models->customer
from django.contrib.auth.hashers import make_password, check_password # for password hashing in admin panel
from store.models.product import Product
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
# from django.utils.decorators import method_decorator


# Cart page
class OrderView(View):
# 
    # @method_decorator(auth_middleware)
    def get(self,request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customers(customer)
        # orders = orders.reverse()
        return render(request,'orders.html',{'orders': orders})