from rest_framework import viewsets, generics, permissions
from .models import User, EmployerProfile, Job, CandidateProfile, JobApplication
from .serializers import CandidateProfileSerializer, JobApplicationSerializer, UserSerializer,RegisterSerializer, EmployerProfileSerializer, JobSerializer
from .permissions import IsEmployer
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EmployerProfileViewSet(viewsets.ModelViewSet):
    queryset = EmployerProfile.objects.all()
    serializer_class = EmployerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-posted_at')
    serializer_class = JobSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated, IsEmployer]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

class CandidateProfileViewSet(viewsets.ModelViewSet):
    queryset = CandidateProfile.objects.all()
    serializer_class = CandidateProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
