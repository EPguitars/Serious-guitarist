from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import BlockForm
from django.views.generic.edit import CreateView
from .models import TrainingBlock
from django.urls import reverse_lazy
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
    blocks = []
    blocks_exist = False
    blocks_count = TrainingBlock.objects.filter(user=request.user).count()
    if TrainingBlock.objects.filter(user=request.user).exists():
        blocks_exist = True    
        
        blocks = TrainingBlock.objects.filter(user=request.user)
    
    context = {
        "blocks" : blocks,
        "blocks_exist" : blocks_exist,
        "blocks_count" : blocks_count
    }
    
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

class BlockCreate(CreateView):
    model = TrainingBlock
    template_name = 'training_room/create_block.html'
    model.user = User
    form_class = BlockForm
    success_url = reverse_lazy('gym')
    