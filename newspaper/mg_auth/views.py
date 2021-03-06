from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from newspaper.settings import LOGIN_URL
from newspaper.mg_auth.forms import SignInForm, RegisterForm


def u_register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(LOGIN_URL)
    else:
        form = RegisterForm()
    context = {
        'form': form,
        'name': 'Registration page'
    }
    return render(request, 'auth/register.html', context)


def sign_in(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = SignInForm()
    context = {
        'form': form,
        'name': 'Sign in page',
    }
    return render(request, 'auth/sign-in.html', context)


@login_required(login_url=LOGIN_URL)
def sign_out(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')
    else:
        return render(request, 'auth/sign-out.html', context={'name': 'Sign out page'})
