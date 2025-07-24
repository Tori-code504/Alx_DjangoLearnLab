from django import forms
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'date_of_birth', 'profile_photo', 'password1', 'password2']
