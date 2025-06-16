from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, EmployerProfileViewSet, JobViewSet, RegisterView, CandidateProfileViewSet, JobApplicationViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'employers', EmployerProfileViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'candidates', CandidateProfileViewSet)
router.register(r'applications', JobApplicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),

]
