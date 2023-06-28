from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register_view(request):
    return render(request, 'accounts/register.html')

def login_view(request):
     return render(request, 'accounts/login.html')

