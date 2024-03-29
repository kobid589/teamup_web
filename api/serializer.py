from rest_framework import serializers

from apps.Room.models import Room


class RoomSerializer(serializers.ModelSerializer):
    logo = serializers.FileField(required=False)

    class Meta:
        model = Room
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    logo = serializers.FileField(required=False)

    class Meta:
        model = Room
        fields = '__all__'


class ToolSerializer(serializers.ModelSerializer):
    logo = serializers.FileField(required=False)

    class Meta:
        model = Room
        fields = '__all__'
