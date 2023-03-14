from django.http import HttpResponse, JsonResponse
from django.urls import path

from apps.Expertise.models import Expertise


def list_room(request):
    expertise_list = Expertise.objects.all()
    payload = []
    for expertise in expertise_list:
        json_data = {
            'id': expertise.id,
            'name': expertise.name,
        }
        payload.append(json_data)
    return HttpResponse(JsonResponse({'payload': payload}))


urlpatterns = [
    path('rooms/list', list_room, name='rooms-list'),
]
