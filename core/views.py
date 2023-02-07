from django.shortcuts import render

# from core.models import Individual


# Create your views here.
from apps.Individual.models import Individual


def index(request):
    individual = Individual.objects.all()[0]
    return render(request, 'index.html', context={'individual': individual})
