from django.shortcuts import render

# from core.models import Individual


# Create your views here.
def index(request):
    # person_list = Individual.objects.all()
    return render(request, 'index.html', context={'list': ''})
