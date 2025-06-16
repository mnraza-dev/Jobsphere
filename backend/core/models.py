
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_employer = models.BooleanField(default=False)

    def __str__(self):
        return self.username
class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employer_profile')
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

