# views.py
import os

from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from rest_framework import permissions, status
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Team.models import Team
from api.serializer import IndividualSerializer, TeamSerializer
from apps.Individual.models import Individual
from teamup_web.settings import auth


class IndividualViewSet(viewsets.ModelViewSet):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer
    permission_classes = [IsAuthenticated]


class TeamView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    def post(self, request, file):
        serializer = TeamSerializer(data=request.data, files=file)
        print("===========Files==============")
        print(request.FILES)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        team = Team.objects.get(pk=pk)
        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        team = Team.objects.get(pk=pk)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def room_api(request):
    if request.method == "POST":
        # sanitize filename to prevent path traversal attacks
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():

            if request.FILES:
                filename = os.path.basename(request.FILES['logo'].name)
                file = ContentFile(request.FILES['logo'].read())
                path = default_storage.save('rooms/' + 'rooms_' + filename, file)
                serializer.validated_data['logo'] = path
            # print(serializer.validated_data['user'])
            serializer.validated_data['user'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "GET":
        teams = Team.objects.filter(user=request.user)
        for team in teams:
            pass
            # print(team)
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def register_user(request):
    """
    API endpoint for user registration.
    """
    email = request.data.get('email')
    password = request.data.get('password')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    id_token = ''

    # Check if user with given email already exists
    if User.objects.filter(email=email).exists():
        return Response({'error': 'User with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        firebase_user = auth.create_user_with_email_and_password(email, password)
        id_token = firebase_user['idToken']
        print(id_token)
        if first_name and last_name:
            auth.update_profile(id_token=firebase_user['idToken'], display_name=first_name + ' ' + last_name)
        # print(firebase_user["idToken"])
    except Exception as e:
        print(e)
        return Response({'error': 'Failed to create Firebase user.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Create user in Django
    try:
        user = User.objects.create_user(username=firebase_user['localId'], email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        token, created = Token.objects.get_or_create(key=firebase_user['localId'], user=user)
    except Exception as e:
        print(e)
        auth.delete_user_account(id_token=firebase_user['idToken'])
        return Response({'error': 'Django Error :: Failed to create django user.'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Create Firebase user
    return Response({'token': token.key, 'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_list(request):
    users = User.objects.filter(is_superuser=False)
    data = {
        'count': users.count(),
        'results': [{
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_staff': user.is_staff,
            'is_active': user.is_active,
            'date_joined': user.date_joined
        } for user in users]
    }
    return Response(data)
