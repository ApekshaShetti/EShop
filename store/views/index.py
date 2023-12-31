from django.shortcuts import render,redirect
from django.http import HttpResponse  # when we route a url what should be on screen particularly a text can be done with this
from store.models.product import Product # importing this to get the data of all product which is present in models->product
from store.models.category import Category # importing this to get the data of all category which is present in models->category
from store.models.customer import Customer # importing this to get the data of all customer which is present in models->customer
from django.contrib.auth.hashers import make_password, check_password # for password hashing in admin panel
from django.views import View

# home page

class Index(View):
    def get(self,request):
        # will create a empty cart initially 
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        all_products = None # when route this page it will call the function from products.py is present in models folder                                                                                                                                                                                                                        
        all_categories = Category.get_all_categories() # when route this page it will call the function from category.py is present in models folder 
        category_id = request.GET.get('category')
        # if category id is passed then only it will show that products with that category id 
        if category_id:
            all_products = Product.get_all_products_by_category_id(category_id)
        # if category id is not selected it will show all products 
        else:
            all_products = Product.get_all_products()
        # data is a dictionary that will contain values of products, categories and any data that is to be shown in index.html 
        data = {}
        data['all_products'] = all_products 
        data['all_categories'] = all_categories 
        print('You are' , request.session.get('email'))
        return render(request,'index.html',data)  # sending all data to index.html file
    


    def post(self,request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        if cart:
            qty = cart.get(product)
            if qty:
                if remove:
                    if qty <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = qty - 1
                else:
                    cart[product] = qty + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('homepage')

    