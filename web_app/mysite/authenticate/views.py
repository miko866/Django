from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    return render(request, 'authenticate/home.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You Have been Logged In!'))
            return redirect('home')
        else:
            messages.success(request, ('Error Loggin In - Please Try Again...'))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out...'))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You have Registered...'))
            return redirect('home')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'authenticate/register.html', context)

def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You have Edited Your Profile...'))
            return redirect('home')
    else:
        form = UserChangeForm(instance=request.user)
    context = {'form': form}
    return render(request, 'authenticate/edit_profile.html', context)
