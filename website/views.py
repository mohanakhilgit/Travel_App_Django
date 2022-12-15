from django.shortcuts import render

from .models import Place, Person

# Create your views here.


def home(request):
    place = Place.objects.all()
    person = Person.objects.all()
    return render(request, 'index.html', {'places': place, 'persons': person})

