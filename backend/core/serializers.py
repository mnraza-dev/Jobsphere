from rest_framework import serializers
from .models import User, EmployerProfile, Job

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_employer']

class EmployerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = EmployerProfile
        fields = ['id', 'user', 'company_name']

class JobSerializer(serializers.ModelSerializer):
    employer = EmployerProfileSerializer()

    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'location', 'posted_at', 'employer']
