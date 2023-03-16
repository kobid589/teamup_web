from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import register_user, room_api, user_list, fetch_room_data, fetch_room_members_list, request_to_join, \
    fetch_user_data, fetch_request_members_list, reject_request, accept_request, fetch_all_team_up_request, \
    remove_member

router = routers.DefaultRouter()


def dummy(request):
    pass


urlpatterns = [
    # Main
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest-framework')),
    path('api-token-auth/', obtain_auth_token, name='api-token_auth'),
    # Users
    path('register/', register_user, name='user-registration'),  # register new user
    path('users/', user_list, name='users'),  # show all users
    path('users/<id>/', fetch_user_data, name='fetch-user-data'),  # get a user detail
    # Room
    path('room/', room_api, name='rooms'),  # get all rooms
    path('room/<int:pk>/', fetch_room_data, name='fetch-room'),  # get a room detail
    path('room/members/<int:pk>/', fetch_room_members_list, name='fetch-room-members'),  # all members
    path('room/requests/<int:pk>/', fetch_request_members_list, name='fetch-request-members'),  # all requested members
    path('room/request/', request_to_join, name='request-to-join'),  # Adds to request list
    path('room/reject/', reject_request, name='reject-request'),  # Removes from request list
    path('room/accept/', accept_request, name='accept-request'),  # Adds member from request list to members list
    path('room/remove-member/', remove_member, name='remove-member'),  # Removes member from team
    path('room/all-requests/', fetch_all_team_up_request, name='all-request'),  # shows all request for current user
    # Skill
    path('skills/', dummy, name='skills'),  #
    # path('skills/add/', dummy, name='skill-add'),  # The superuser predefines skills
    path('skills/<id>', dummy, name='skill-detail'),  #
    path('skills/<id>', dummy, name='skill-update'),  #
    path('skills/<id>/delete', dummy, name='skill-delete'),  #
    # Tools

    # Organizations
]
