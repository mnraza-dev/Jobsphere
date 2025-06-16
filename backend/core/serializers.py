from rest_framework import serializers
from .models import User, EmployerProfile, Job, CandidateProfile, JobApplication
from django.contrib.auth import get_user_model

User = get_user_model()
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_employer']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_employer=validated_data['is_employer']
        )
        return user

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


class CandidateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateProfile
        fields = '__all__'

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'
