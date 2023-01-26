from django.shortcuts import render
from django.http import HttpResponse
from apps.Individual.models import Individual


def profile(request):
    info_list = Individual.objects.all()
    return render(request, 'profiles.html',
                  {'info_list': info_list})
