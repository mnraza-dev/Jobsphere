from rest_framework import viewsets, generics
from .models import User, EmployerProfile, Job
from .serializers import UserSerializer,RegisterSerializer, EmployerProfileSerializer, JobSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EmployerProfileViewSet(viewsets.ModelViewSet):
    queryset = EmployerProfile.objects.all()
    serializer_class = EmployerProfileSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-posted_at')
    serializer_class = JobSerializer
