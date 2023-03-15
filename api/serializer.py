from django.contrib.auth.models import User
from rest_framework import serializers

from Team.models import Team
from apps.Individual.models import Individual


class IndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individual
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    logo = serializers.FileField(required=False)

    class Meta:
        model = Team
        fields = '__all__'
