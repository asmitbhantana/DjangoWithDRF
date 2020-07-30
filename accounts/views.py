from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.forms import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model

from .forms import LoginForm, RegisterForm

User = get_user_model()


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user:
                print("User exists", user)
                login(request, user)
                return redirect('account:profile')
            else:
                form.add_error('username', "Error On Credentials")
                print("Auth credentials doesn't matches")
            print("Valid Form")
        print(request.POST)
    elif request.method == 'GET':
        form = LoginForm()

    return render(request, 'accounts/login.html', {'loginform': form})


def profile_view(request):
    if request.user.is_authenticated:
        # this is passed fot a context a[[
        from statusapp.models import StatusMessage
        messages = StatusMessage.objects.filter(user=request.user)
        return render(request, 'accounts/profile.html', {'user': request.user, 'message': messages})
    else:
        return redirect('account:login')


def logout_view(request):
    logout(request)
    return redirect('account:login')


def register_view(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            print("Valid data")
            cleaned_data = register_form.cleaned_data
            new_user = User(first_name=cleaned_data['first_name'], last_name=cleaned_data['last_name'],
                            email=cleaned_data['email'], username=cleaned_data['username'])
            new_user.save()
            new_user.set_password(cleaned_data['password'])
            new_user.save()

            return redirect('account:login')
    elif request.method == 'GET':
        register_form = RegisterForm()

    return render(request, 'accounts/register.html',
                  {
                      'registerform': register_form,
                  })
