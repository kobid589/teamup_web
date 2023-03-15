from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views
from .views import register_user, room_api, user_list

router = routers.DefaultRouter()
router.register(r'individuals', views.IndividualViewSet, basename="individual")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('register/', register_user, name='user_registration'),
    path('room/', room_api, name='rooms'),
    path('users/', user_list, name='users'),
    # path('rooms/', TeamView.as_view(), name='team'),
    # path('cfu/', create_firebase_user, name='sync'),

]
