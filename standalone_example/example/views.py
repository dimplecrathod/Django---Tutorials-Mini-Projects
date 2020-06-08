from django.shortcuts import render, redirect

from .forms import AnagramForm

def index(request):
    if request.method == 'POST':
        form = AnagramForm(request.POST)

        if form.is_valid():
            redirect('index')
        
        else:
            form = AnagramForm()

        context = {'form': form}

        return render(request, 'index.html', context)

# Create your views here.
