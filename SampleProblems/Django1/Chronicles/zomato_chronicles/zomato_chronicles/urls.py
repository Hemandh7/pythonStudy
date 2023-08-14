# zomato_chronicles/urls.py

from django.contrib import admin
from django.urls import path, include  # Include 'include' here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurant.urls')),  # Include app's URLs at the root URL
]
