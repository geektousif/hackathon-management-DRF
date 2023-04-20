from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Hackathon, Enrollment
from users.serializers import UserSerializer

User = get_user_model()


class HackathonSerializer(serializers.ModelSerializer):
    host = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Hackathon
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    hackathon = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Enrollment
        fields = '__all__'
