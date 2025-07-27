from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'bookshelf/register.html', {'form': form})

