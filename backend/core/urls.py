from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, EmployerProfileViewSet, JobViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'employers', EmployerProfileViewSet)
router.register(r'jobs', JobViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
