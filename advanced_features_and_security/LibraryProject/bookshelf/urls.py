from django.urls import path
from .views import register_view
from . import views

urlpatterns = [
    path('register/', register_view, name='register'),
    path('', views.book_list, name='book_list'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
    path('example-form/', views.example_form_view, name='example_form'),
]
