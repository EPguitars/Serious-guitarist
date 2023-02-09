from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import BlockForm
from .models import TrainingBlock
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ( 
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    ListView
)

# It's a FBV for the home page. It consist a login form also!

def main(request):
    if request.user.is_authenticated:
        return redirect('list_blocks')
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
            return redirect('list_blocks')
        else:
            messages.error(request, 'Username or password does not correct')
    context = {}
    
    return render(request, 'training_room/home.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

# User's profile FBV
# testing 


# A FBV for user registration page 

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

# A CBV for creating a new block

class BlockCreate(CreateView):
    model = TrainingBlock
    template_name = 'training_room/create_block.html'
    form_class = BlockForm
    success_url = reverse_lazy('list_blocks')
    
    # New block will belong to the authorised user 
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BlockCreate, self).form_valid(form)

# Here I'm rendering a page for experiments with html and css. Will be deleted when the project will be done!

def card(request):
    return render(request, 'training_room/card.html')


# A CBV for editing a block

class UpdateBlock(UpdateView):
    model = TrainingBlock
    template_name = 'training_room/update_card.html'
    form_class = BlockForm
    success_url = reverse_lazy('list_blocks')
    context_object_name = "blocks"



class ListBlocks(LoginRequiredMixin, ListView):

    template_name = "training_room/gym.html"
    queryset = TrainingBlock.objects.all()
    
        
    def get_queryset(self):
        return TrainingBlock.objects.filter(user=self.request.user).order_by('created')


class DeleteBlocks(DeleteView):
    template_name = 'training_room/delete_block.html'
    model = TrainingBlock
    success_url = reverse_lazy('list_blocks')
    context_object_name = "block_on_delete"