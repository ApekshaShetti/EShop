from django.shortcuts import render,redirect
from django.http import HttpResponse  # when we route a url what should be on screen particularly a text can be done with this
from .models.product import Product # importing this to get the data of all product which is present in models->product
from .models.category import Category # importing this to get the data of all category which is present in models->category
from .models.customer import Customer # importing this to get the data of all customer which is present in models->customer
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

# home page 
def index(request):   # function to show what should be there when i write localhost:8000 or home page
    # return HttpResponse('<h1> Index Page</h1>')
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

    return render(request,'index.html',data)  # sending all data to index.html file

# validation

def validateCustomer(first_name,last_name,phone,password,email,customer):
    error_msg = None
    if not first_name:
            error_msg = "First Name Required"
    elif len(first_name) < 3:
        error_msg = "First Name should be 3 char long or more"
    elif not last_name:
        error_msg = "Last Name Required"
    elif len(last_name) < 3:
        error_msg = "First Name should be 3 char long or more"
    elif not phone:
        error_msg = "Phone Number Required"
    elif len(phone) < 10:
        error_msg = "Enter Valid Phone Number"
    elif len(password) < 7:
        error_msg = "Password should be 7 char long or more"
    elif len(email) < 7:
        error_msg = "Email should be 7 char long or more"
    elif customer.isExists():
        error_msg = 'Email Already Registered'
    
    return error_msg



def registerUser(request):
    post_data = request.POST
    first_name = post_data.get('fname')
    last_name = post_data.get('lname')
    phone = post_data.get('phone')
    email = post_data.get('email')
    password = post_data.get('password')

    # Storing this data in a value dictionary so that these data can be stored in a form even if any field is empty
    value = {
        'first_name' : first_name,
        'last_name' : last_name,
        'phone' : phone,
        'email' : email,
        'password' : password,
    }

    error_msg = None

    # customer object
    customer = Customer(first_name=first_name,
                        last_name=last_name,
                        phone=phone,
                        email=email,
                        password=password)

    error_msg = validateCustomer(first_name,last_name,phone,password,email,customer)

    # Saving after validation 
    if not error_msg:
        customer.password = make_password(customer.password)  # hashing the password in admin panel
        customer.register()  # calling this function which is present in customer.py
        return redirect('homepage')   # home page is the name given to index page which is present in urls.py 
    else:
        data = {
            'error' : error_msg,
            'values' : value
        }
        return render(request, 'signup.html',data)

# signup page 

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        return registerUser(request)
       