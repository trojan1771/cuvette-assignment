# user_auth/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            # Check if the username or email is already registered
            if UserProfile.objects.filter(username=username).exists():
                form.add_error('username', 'This username is already registered. Please choose a different one.')
                return render(request, 'user_auth/register.html', {'form': form})

            if UserProfile.objects.filter(email=email).exists():
                form.add_error('email', 'This email is already registered. Please use a different email.')
                return render(request, 'user_auth/register.html', {'form': form})

            user = form.save()  # Save the user
            # Create a user profile
            UserProfile.objects.create(username=username, email=email, password=user.password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'user_auth/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username']  # It can be either username or email
            password = form.cleaned_data['password']

            # Try to authenticate the user
            user = authenticate(request, username=username_or_email, password=password)

            # Check if the authentication was successful
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                form.add_error('password', 'Invalid login credentials. Please try again.')

    else:
        form = LoginForm()
    return render(request, 'user_auth/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'user_auth/dashboard.html')

@login_required
def user_profile(request):
    return render(request, 'user_auth/profile.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
