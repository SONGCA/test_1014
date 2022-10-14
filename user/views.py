from django.shortcuts import render
from .models import User

# Create your views here.
def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    elif  request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
    
def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')