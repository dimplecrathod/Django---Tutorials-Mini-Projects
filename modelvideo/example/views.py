from django.shortcuts import render
from django.views import viewsfrom 
from .models import Car
from .forms import UsernameForm, CarForm

def index(request):
    if request.method == 'POST':
        form = UsernameForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data['username'])
        else:
            print('FORM IS NOT VALID'
            )
    else:
        form = UsernameForm()
    
    context = {'form': form}

    return render(request, 'example/form.html', context)


def car(request):
    if request.method == 'POST':
        car = Car.objects.get(pk=2)
        form = CarForm(request.POST, instance = car)

        if form.is_valid():
            print(form.cleaned_data['name'])
            form.save()
        else:
            form = CarForm()

    context = {'form': form}

    return render(request, 'example/car.html', context)


class CarView(View):
    form = self.form_class()
    model = Car
    template_name = 'example/car.html'

    def get(self, request):
        form = self.form_class()

        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        car = Car.objects.get(pk=2)
        form = self.form_class(request.POST, instance=car)

        if form.is_valid():
            print(form.cleaned_data['name'])
            form.save()

        context = {'form': form}

        return render(request, self.template_name, context)


# Create your views here.
