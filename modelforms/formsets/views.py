from django.shortcuts import render, redirect
from django.forms import modelformset_factory, inlineformset_factory
from .models import Example, Programmer, Language

def index(request):
    ExampleFormSet = modelformset_factory(Example, fields= ('name', 'location'), extra=4)
    
    if request.method == 'POST':
        form = ExampleFormSet(request.POST)
        #to save individual submits
        #instances = form.save(commit=False)

        #for instance in instances:
            #instance.save()
        
        instances = form.save()

    form = ExampleFormSet()
    
    #form = ExampleFormSet(queryset = Example.objects.none())

    ##queryset = Example.objects.none() means it will render form with empyt fields and not data from database

    return render(request, 'index.html', {'form': form})
# Create your views here.


def ifchanged(request):
    # values = ['Python', 'Ruby', 'JavaScript'],
    # context = {'values': values}
    dict_values =[{"name": "Dimple", "language": "Python"},
                    {"name": "Dimple", "language": "Flask"},
                    {"name": "Devangi", "language": "Java"},
                    {"name": "Maria", "language": "C"},
                    {"name": "Pedro", "language": "C++"}
                ]
    context = { 
        "values" : dict_values
        #["Python", "Python", "Python", "Ruby", "JavaScript", "JavaScripts"], 
    }
    return render(request, 'ifchanged.html', context)

def prog(request, programmer_id):
        programmer = Programmer.objects.get(pk=programmer_id)
        #LanguageFormset = modelformset_factory(Language, fields=('name',))
        LanguageFormset =inlineformset_factory(Programmer, Language, fields=('name',), can_delete=False, extra=1, max_num=5)
        
        if request.method == 'POST':
            #formset = LanguageFormset(request.POST,queryset = Language.objects.filter(programmer__id=programmer.id))
            formset = LanguageFormset(request.POST, instance=programmer)
            if formset.is_valid():
                #instances = formset.save(commit=False)
                #for instance in instances :
                    #instance.programmer_id = programmer.id
                    #instance.save()
                formset.save()
                return redirect('prog', programmer_id=programmer.id)

        #formset = LanguageFormset(queryset = Language.objects.filter(programmer__id=programmer.id))
        formset = LanguageFormset(instance=programmer)

        return render(request, 'prog.html', {'formset': formset})
