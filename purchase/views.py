from django.shortcuts import render, redirect
from django.contrib.auth import login,logout

# Create your views here.
def home(request):
    return render(request, template_name = 'index.html')

def logout_user(request):
    logout(request)
    return redirect('home')