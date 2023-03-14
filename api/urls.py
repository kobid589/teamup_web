
from django.urls import path
from api.views import list_room, list_of_organization,\
    list_of_highlights, list_of_awards, list_of_skills,list_of_experiences


urlpatterns = [
    path('rooms/list', list_room, name='rooms-list'),
    path('organisation', list_of_organization, name='org_list'),
    path('highlights', list_of_highlights, name='highlights'),
    path('awards', list_of_awards, name='awards'),
    path('skills', list_of_skills, name='skills'),
    path('experiences', list_of_experiences, name='experiences')
]
