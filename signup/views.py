from django.shortcuts import render


# Create your views here.
def makesignup(request):
    return render(request, 'signup.html')

