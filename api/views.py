# views.py
import os

from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db.models import Q
from rest_framework import permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.Room.models import Room
from api.serializer import RoomSerializer
from teamup_web.settings import auth


# =========================================
#
# ROOM
#
# =========================================


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
# Create a room and view all rooms.
# TESTED √
def room_api(request):
    if request.method == "POST":
        # sanitize filename to prevent path traversal attacks
        print("\n --------- Current user ---------\n")
        print(request.user)
        serializer = RoomSerializer(data=request.data)
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
        rooms = Room.objects.filter(Q(user=request.user) | Q(members__username=request.user.username))
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)


# Fetch room data.
# TESTED √
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_room_data(request, pk):
    room = Room.objects.get(pk=pk)
    if room:
        serializer = RoomSerializer(room)
        return Response(serializer.data, status.HTTP_200_OK)
    return Response({'message': 'Data not found'}, status.HTTP_500_INTERNAL_SERVER_ERROR)


# Fetch room member list.
# √ TESTED
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_room_members_list(request, pk):
    room = Room.objects.get(pk=pk)
    return Response(get_user_json_from_list(room.members.all()))


# Fetch request member list.
# √ TESTED
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_request_members_list(request, pk):
    room = Room.objects.get(pk=pk)
    return Response(get_user_json_from_list(room.request_members.all()))


# Request a member to join room
# √ TESTED
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def request_to_join(request):
    uid = request.data['uid']
    room_id = request.data['room_id']
    room = Room.objects.get(id=room_id)
    user = User.objects.get(username=uid)
    if room and user:
        if room.request_members.contains(user):
            return Response({'message': 'Already sent request'}, status.HTTP_200_OK)
        if not room.members.contains(user):
            room.request_members.add(user)
            room.save()
            return Response({'message': 'Request sent'}, status.HTTP_200_OK)
        return Response({'message': 'Already a member'}, status.HTTP_200_OK)
    return Response({'message': 'Couldn\'t send room up request'}, status.HTTP_500_INTERNAL_SERVER_ERROR)


# Reject a member request
# √ TESTED
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reject_request(request):
    room_id = request.data['room_id']
    uid = request.data['uid']
    room = Room.objects.get(id=room_id)
    user = User.objects.get(username=uid)
    if room and user:
        if room.request_members.contains(user):
            room.request_members.remove(user)
            room.save()
            return Response({'message': 'Request Removed'}, status.HTTP_200_OK)
        return Response({'message': 'No request found'}, status.HTTP_200_OK)
    return Response({'message': 'Could not reject room up request'}, status.HTTP_500_INTERNAL_SERVER_ERROR)


# Accept a member request
# √ TESTED
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def accept_request(request):
    room_id = request.data['room_id']
    uid = request.data['uid']
    room = Room.objects.get(id=room_id)
    user = User.objects.get(username=uid)
    if room and user:
        if room.members.contains(user):
            return Response({'message': 'User is already a member'}, status.HTTP_200_OK)
        room.members.add(user)
        room.request_members.remove(user)
        return Response({'message': 'Request accepted'}, status.HTTP_200_OK)
    return Response({'message': 'Could not accept room up request'}, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def remove_member(request):
    room_id = request.data['room_id']
    uid = request.data['uid']
    room = Room.objects.get(id=room_id)
    user = User.objects.get(username=uid)
    if room and user:
        if room.members.contains(user):
            room.members.remove(user)
            room.save()
            return Response({'message': 'Removed from room'}, status.HTTP_200_OK)
        return Response({'message': 'User is not a member'}, status.HTTP_200_OK)
    return Response({'message': 'Could not accept room up request'}, status.HTTP_500_INTERNAL_SERVER_ERROR)


# Fetch all room up request
# √ TESTED
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_all_team_up_request(request):
    user = request.user
    rooms = Room.objects.filter(Q(request_members__isnull=False) & Q(request_members__username=user.username))
    print(rooms)
    print(len(rooms))
    if len(rooms) > 0:
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    return Response({'message': 'No Request Found.', 'user': get_user_json(user)},
                    status.HTTP_500_INTERNAL_SERVER_ERROR)


# =========================================
#
# USER
#
# =========================================

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
        if first_name and last_name:
            auth.update_profile(id_token=firebase_user['idToken'], display_name=first_name + ' ' + last_name)
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
    users = User.objects.filter(Q(is_superuser=False) & ~Q(username=request.user.username))
    return Response(get_user_json_from_list(users))


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_user_data(request, id):
    user = User.objects.get(username=id)
    if not user:
        return Response({'message': 'No users found'}, status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(get_user_json(user), status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user_data(request, id):
    user = User.objects.get(username=id)
    try:
        user.delete()
        return Response({'message': 'Successfully deleted user.'}, status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({'message': 'Couldn\'t delete user.'}, status.HTTP_500_INTERNAL_SERVER_ERROR)


# ..........................................
#
# Helper Functions
#
# ..........................................
def get_user_json(user):
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'is_staff': user.is_staff,
        'is_active': user.is_active,
        'date_joined': user.date_joined
    }


def get_user_json_from_list(users):
    data = {
        'count': users.count(),
        'results': [get_user_json(user) for user in users]
    }
    return data

# =========================================
#
# Skills
#
# =========================================

# Add Skills to user

# Get user specific skills

# Filter User by skills

#
