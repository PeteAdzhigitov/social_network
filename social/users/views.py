from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomRegistrationForm

# Create your views here.

def registration(request):
    form = CustomRegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'User {username} has been created')
            return redirect('login')


    return render(request, 'users/registration.html' , {'form':form})