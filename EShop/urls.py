from django.contrib import admin
from django.urls import path,include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('store.urls')),  # function to include the url that is present in store application for a home page in urls.py of store
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)    # used this + button to show the url of image and chnage the url of image a bit media root and media url are in settings.py
