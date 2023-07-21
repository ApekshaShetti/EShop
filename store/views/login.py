from django.views import View
from django.shortcuts import render,redirect, HttpResponseRedirect
from store.models.customer import Customer # importing this to get the data of all customer which is present in models->customer
from django.contrib.auth.hashers import make_password, check_password # for password hashing in admin panel

# login page
class Login(View):
    return_url = None
    def get(self,request):
        Login.return_url = request.GET.get('return_url')
        return render(request,'login.html')
    
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        customer = Customer.getCustomerByEmail(email)   # calling the function which is present in customer.py file
        error_msg = None

        if customer:
            flag = check_password(password,customer.password)
            if flag:
                request.session['customer'] = customer.id

                # if middleware is used then we will be redirect to order page 
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                # if not go directly to index page 
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_msg = "Email/Password is Invalid"        
        else:
            error_msg = "Email/Password is Invalid"        
        return render(request, 'login.html', {'error' : error_msg})



def logout(request):
    request.session.clear()
    return redirect('login')
        
    
