from django.shortcuts import render
from login.models import login


# Create your views here.
def makelogin(request):
    return render(request, 'index.html')


def logincomplete(request):
    if request.method == "POST":
        user = request.POST.get('username_email')
        password = request.POST.get('password')
    data = login(username_email=user, password=password)
    data.save()

    return render(request, 'welcome.html')
