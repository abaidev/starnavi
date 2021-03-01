from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import (get_user_model, authenticate,
                                 login, logout)
from .forms import UserCreateForm

User = get_user_model()

def index(request):
    return render(request, 'index.html', {})

def signup(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are logged in already')
        return redirect('socialnet:home')

    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('socialnet:home')
    return render(request, "signup.html", {'form': form})

def loginView(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are logged in already')
        return redirect('socialnet:home')

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('socialnet:home')
        else:
            messages.warning(request, "Username OR Password is incorrect")
    return render(request, "login.html", {})

def logoutUser(request):
    logout(request)
    return redirect("socialnet:login")
