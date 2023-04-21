from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


# Create your models here.

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **other_fields):

        if not email:
            raise ValueError(_("Email is required"))
        if not password:
            raise ValueError(_("Password is required"))

        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **other_fields)


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(
        verbose_name="email address",  max_length=255, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    # TODO: can_host flag to be added
    can_host = models.BooleanField(default=False)

    object = CustomUserManager()

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
