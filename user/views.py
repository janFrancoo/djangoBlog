from django.shortcuts import render
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

def register(request):
    form = forms.RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")

        newUser = User(username = username, email = email)
        newUser.set_password(password)
        newUser.save()
        login(request, newUser)
        messages.warning(request, "Başarıyla kayıt oldunuz!")
        return redirect("index")
    
    context = {
        "form": form
    }
    return render(request, "register.html", context)

def loginUser(request):
    form = forms.LoginForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username, password = password)

        if user is None:
            messages.warning(request, "Kullanıcı adı veya şifre hatalı!")
            return render(request, "login.html", context)
        
        login(request, user)
        messages.success(request, "Başarıyla giriş yaptınız...")
        return redirect("index")

    return render(request, "login.html", context)

def logoutUser(request):
    logout(request)
    messages.success(request, "Başarıyla çıkış yapıldı!")
    return redirect("index")