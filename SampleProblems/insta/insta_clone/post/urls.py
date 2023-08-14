from django.urls import path
from . import views


urlpatterns = [
    path('create_post/', views.create_post,name='create_post'),
    path('view_posts/', views.view_posts,name='view_posts'),
    path('delete_post/', views.delete_post,name='delete_post'),

]
