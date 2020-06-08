from django.shortcuts import render
import datetime

def index(request):
    now=datetime.datetime.now() 
    context = {
        'first' : 5,
        'second' : 56789090,
        'third' : 12,
        'now': now,
        'other_date' : now - datetime.timedelta(days=1),
        'future': now + datetime.timedelta(days=542),
        'past': now - datetime.timedelta(days=14),
    }
    return render(request, 'app.html', context)

# Create your views here.
