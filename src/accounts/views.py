from django.shortcuts import render, redirect
from django.contrib.auth import (
    logout as logout_user, login as login_user
)
from django.contrib import messages

from .forms import CustomUserCreationForm, LoginForm


def register(request):
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login_user(request, user)
        messages.success(request, 'You successfully registered!')
        return redirect('home')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login(request):
    form = LoginForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def logout(request):
    logout_user(request)
    messages.info(request, 'User logged out!')
    return redirect('login')
