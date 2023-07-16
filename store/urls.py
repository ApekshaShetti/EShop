from django.contrib import admin
from django.urls import path
from .views import index
from .views import signup
from.views import login

urlpatterns = [
    path('',index), # calling the index function that is present in views.py to show the data when i route localhost:8000
    path('signup',signup), # calling the signup function that is present in views.py to show the signup page when i route localhost:8000
    path('login',login)
]
