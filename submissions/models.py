from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.auth import get_user_model

from hackathons.models import Hackathon

User = get_user_model()


class Image(models.Model):
    image = models.ImageField(upload_to='images/submissions/')


class File(models.Model):
    file = models.FileField(upload_to='files/submissions/')


class Link(models.Model):
    link = models.URLField()


class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE, related_name='hackathon')
    name = models.CharField(max_length=255)
    summary = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

