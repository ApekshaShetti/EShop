from django.contrib import admin
from django.urls import path
from .views import index, login, signup

urlpatterns = [
    path('',index.Index.as_view(), name='homepage'), # calling the index function that is present in views.py to show the data when i route localhost:8000
    path('signup',signup.SignUp.as_view(), name ='signup'), # calling the Signup class that is present in views.py to show the signup page when i route localhost:8000
    path('login',login.Login.as_view(), name = 'login')
]
