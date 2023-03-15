from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from login.models import login
import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.
from teamup_web.settings import firebaseConfig


def makelogin(request):
    return render(request, 'login.html')


def logincomplete(request):
    if request.method == "POST":
        user = request.POST.get('username_email')
        password = request.POST.get('password')
    data = login(username_email=user, password=password)
    data.save()

    return render(request, 'welcome.html')


@login_required
def create_firebase_user(request):
    user = request.user
    # Build the request URL
    url = f'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=' + firebaseConfig['apiKey']
    # Set the request headers
    headers = {'Content-type': 'application/json'}
    # Set the request body with the user data
    data = {
        'email': user.email,
        'password': user.password,
        'displayName': user.get_full_name(),
    }
    # Make the request
    response = requests.post(url, headers=headers, json=data)
    # Check the response status code
    if response.status_code == 200:
        # Set the Firebase user UID as the Django user password
        user.password = response.json()['localId']
        user.save()
        return HttpResponse('<b style="colors:darkgreen">User synced!</b>')
    else:
        return HttpResponse('<b style="colors:darkred">Something went wrong</b><br>Status Code : ' + str(response.status_code))
