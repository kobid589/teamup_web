from django.shortcuts import render

# Create your views here.
def makelogin(request):
    return render(request ,'index.html')
