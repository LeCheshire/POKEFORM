from django.shortcuts import render, redirect
from .models import Pokemon
from .forms import PokeForm
# Create your views here.

def home(request):
    pokemons = Pokemon.objects.all()

    context = {
        'pokemons': pokemons,
    }

    return render(request, 'app/home.html', context)


def PokeAdd(request):
    if request.method == 'POST':
        form = PokeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PokeForm()
    context = {'form': form}
    
    return render(request, 'app/PokeAdd.html', context)
