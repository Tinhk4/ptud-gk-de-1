# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/new/', views.create_post, name='create_post'),
    path('post/edit/<int:pk>/', views.edit_post, name='edit_post'),
    path('post/delete/<int:pk>/', views.delete_post, name='delete_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), 

    path('register/', views.register, name='register'),
]
