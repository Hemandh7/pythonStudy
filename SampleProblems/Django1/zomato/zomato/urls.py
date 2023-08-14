from django.contrib import admin
from django.urls import path, include
from menu import views as menu_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', include('menu.urls')),
    path('', menu_views.menu, name='home'),
]
