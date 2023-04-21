from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

SUBMISSION_TYPES = (
    ('image', 'Image'),
    ('file', 'File'),
    ('link', 'Link')
)

User = get_user_model()


class Hackathon(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    background_image = models.ImageField(
        upload_to='hackathons/images/background_image/', blank=True, null=True)
    hackathon_image = models.ImageField(
        upload_to='hackathons/images/hackathon_image/', blank=True, null=True)
    submission_type = models.CharField(
        max_length=20, choices=SUBMISSION_TYPES)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    reward_prize = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.hackathon}"
