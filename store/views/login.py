from django.views import View
from django.shortcuts import render,redirect
from store.models.customer import Customer # importing this to get the data of all customer which is present in models->customer
from django.contrib.auth.hashers import make_password, check_password # for password hashing in admin panel

# login page
class Login(View):
    def get(self,request):
        return render(request,'login.html')
    
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        customer = Customer.getCustomerByEmail(email)   # calling the function which is present in customer.py file
        error_msg = None

        if customer:
            flag = check_password(password,customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['email'] = customer.email
                return redirect('homepage')
            else:
                error_msg = "Email/Password is Invalid"        
        else:
            error_msg = "Email/Password is Invalid"        
        return render(request, 'login.html', {'error' : error_msg})

        
    
