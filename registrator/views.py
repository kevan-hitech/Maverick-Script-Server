from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as django_logout
from .forms import HomeForm, LoginsForm
from django.contrib.auth.models import User

def HomeView(request):
    template_name = 'registration/reg.html'
    form = HomeForm(request.POST or None)
    if form.is_valid():
        usern = request.POST.get('username')
        passw = request.POST.get('password')
        try:
            user = authenticate(username=usern, password=passw)
            if user:
                if user.is_active:
                    login(request, user)
                    request.session['id'] = passw
                    return redirect('/')
        except Exception as e:
            print(e)
    try:
        args = {'form': form, 'e':e}
    except:
        args = {'form': form,}
    return render(request, template_name, args)

def LoginsView(request):
    template_name = 'registration/login.html'
    form = LoginsForm(user=request.user, data=request.POST or None)
    if form.is_valid():
        usern = request.POST.get('username')
        passw = request.POST.get('password')
        try:
            user = authenticate(username=usern, password=passw)
            if user:
                if user.is_active:
                    login(request, user)
                    request.session['id'] = passw
                    return redirect('/')
        except Exception as e:
            print(e)
    try:
        args = {'form': form, 'e':e}
    except:
        args = {'form': form,}
    return render(request, template_name, args)


def logout(request):
    django_logout(request)
    return redirect('/')
