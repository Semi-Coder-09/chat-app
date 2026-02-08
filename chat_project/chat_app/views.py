from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import User_data, Chat, BlockedUser
# Create your views here.
def home(request):
    return render(request, 'base.html')
def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        # save the data to the database
        user = User_data(name=name, email=email, password=password, phone=phone)
        user.save()
        
    return render(request, 'signup.html')
def chat(request):
    return render(request, 'chat.html')
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # authenticate the user
        try:
            user = User_data.objects.get(email=email, password=password)
            return redirect('chat')
        except User_data.DoesNotExist:
            return HttpResponse("Invalid email or password.")
    return render(request, 'login.html')