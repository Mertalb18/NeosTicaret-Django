from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout

def userRegister(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            print('Kullanıcı oluşturuldu')
            return redirect('login')
        
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def userLogin(request):
    if request.method == "POST":
        kullanici = request.POST['kullanici']
        sifre = request.POST['sifre']

        user = authenticate(request, username = kullanici, password = sifre)

        if kullanici is not None:
            login(request, user)
            return redirect('home')
        
    return render(request, 'login.html')

def userLogout(request):
    logout(request)
    return redirect('home')
