
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# User Registration View
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        # Create a new user
        User.objects.create_user(username=username, email=email, password=password1)
        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')

    return render(request, 'accounts/register.html')


# Login View
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('songs')  # Redirect to the songs page after login
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('login')

    return render(request, 'accounts/login.html')


# Logout View
def logout_page(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')
