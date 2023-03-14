from django.shortcuts import render
from apps.Expertise.models import Expertise
from apps.Organization.models import Organization
from apps.Highlights.models import Highlights
from apps.awards.models import Awards
from Skills.models import Skills
from Experience.models import Experience
from django.http import HttpResponse, JsonResponse


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


def list_of_organization(request):
    organisation_list = Organization.objects.all()
    payload = []
    for organisation in organisation_list:
        json_data = {
            'name': organisation.name,
            'logo': organisation.logo.url,
            'description': organisation.description,
            'established_date': organisation.established_date
        }
        payload.append(json_data)
    return HttpResponse(JsonResponse({'payload': payload}))


def list_of_highlights(request):
    highlights_list = Highlights.objects.all()
    payload = []
    for Highlight in highlights_list:
        json_data = {
            'title': Highlight.title,
            'description': Highlight.description,
            'images': Highlight.highlights_images.url
        }
        payload.append(json_data)
    return HttpResponse(JsonResponse({'payload': payload}))


def list_of_awards(request):
    awards_list = Awards.objects.all()
    payload = []
    for award in awards_list:
        json_data = {
            'title': award.title,
            'description': award.description,
            'awarded_on': award.awarded_on,
            'award_logo': award.award_logo.url,
            'award_images': award.award_images.url
        }
        payload.append(json_data)
    return HttpResponse(JsonResponse({'payload': payload}))


def list_of_skills(request):
    skills_list = Skills.objects.all()
    payload = []
    for skills in skills_list:
        json_data = {
            'Skill_type': skills.skill_name,
            'Skill_level': skills.skill_level
        }
        payload.append(json_data)
    return HttpResponse(JsonResponse({'payload': payload}))


def list_of_experiences(request):
    experiences_list = Experience.objects.all()
    payload = []
    for exp in experiences_list:
        json_data = {
            'Started_from': exp.From,
            'Ended_at': exp.To,
            'Description': exp.description,
            'Organisation': {
                'name': exp.organization.name,
                'logo': exp.organization.logo.url,
                'description': exp.organization.description,
                'established_date': exp.organization.established_date
            },
            'Highlights': {
                'title': exp.highlights.title,
                'description': exp.highlights.description,
                'images': exp.highlights.highlights_images.url
            }
        }
        payload.append(json_data)
    return HttpResponse(JsonResponse({'payload': payload}))






