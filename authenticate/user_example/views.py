from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import UserProfileForm

def index(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'not logged in'
    context = {'username': username}
    return render(request, 'user_example/index.html', context)


@login_required
def profile(request):
    return render(request, 'user_example/profile.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid:
            form.save()
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            password
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
            form = UserCreationForm()
            profile_form = UserProfileForm()
        
    context ={'form' : form, 'profile_form': profile_form}
    return render(request, 'registration/register.html', context)