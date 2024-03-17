from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate

# Create your views here.
def home(request):
    return render(request, template_name = 'index.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next = request.GET.get('next')
            return redirect(next or 'home')
        else:
            return redirect('login')
    else:
        return render(request, template_name = 'login.html')