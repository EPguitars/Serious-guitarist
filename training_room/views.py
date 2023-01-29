from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def main(request):
    if request.user.is_authenticated:
        return redirect('gym')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('gym')
        else:
            messages.error(request, 'Username or password does not correct')
    context = {}
    
    return render(request, 'training_room/home.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')


@login_required(login_url='home')
def gym(request):
    context = {}
    
    return render(request, 'training_room/gym.html', context)

def registration(request):
    
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error was accured")

    context = {'form': form}
    return render(request, 'training_room/registration.html', context)