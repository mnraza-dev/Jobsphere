
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

class Job(models.Model):
    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.TextField(blank=True)
    skills = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Candidate: {self.user.username}"
class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE)
    cover_letter = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate.user.username} applied to {self.job.title}"
