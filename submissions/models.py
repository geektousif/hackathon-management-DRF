from django.db import models
from django.contrib.auth import get_user_model

from hackathons.models import Hackathon

User = get_user_model()


def submission_path(instance, filename):
    return f"{instance.hackathon.submission_type}/submissions/hackathon_{instance.hackathon.title}/{instance.user.email.split('@')[0]}/{filename}"


class Submission(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    hackathon = models.ForeignKey(
        Hackathon, on_delete=models.CASCADE, related_name='hackathon')
    name = models.CharField(max_length=255)
    summary = models.TextField()
    submission_image = models.ImageField(
        upload_to=submission_path, null=True, blank=True)
    submission_file = models.FileField(
        upload_to=submission_path, null=True, blank=True)
    submission_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.hackathon} submission"
