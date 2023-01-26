from django.shortcuts import render

# Create your views here.

def main(request):
    context = {}
    
    return render(request, 'training_room/home.html', context)

def gym(request):
    context = {}
    
    return render(request, 'training_room/gym.html', context)