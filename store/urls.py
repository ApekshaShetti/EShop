from django.contrib import admin
from django.urls import path
from .views import index, login, signup,cart
from .views.login import logout 
from .views.checkout import Checkout 
from .views.orders import OrderView
from .middlewares.auth import auth_middleware


urlpatterns = [
    path('',index.Index.as_view(), name='homepage'), # calling the index function that is present in views.py to show the data when i route localhost:8000
    path('signup',signup.SignUp.as_view(), name ='signup'), # calling the Signup class that is present in views.py to show the signup page when i route localhost:8000
    path('login',login.Login.as_view(), name = 'login'),
    path('logout', logout, name = 'logout'),
    path('cart', cart.Cart.as_view(), name = 'cart'),
    path('checkout', Checkout.as_view(), name = 'checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name = 'orders'),

]
