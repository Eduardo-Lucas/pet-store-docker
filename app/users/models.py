from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.query import QuerySet
from django.utils import timezone
from django.urls import reverse
from core.choices import UnidadeFederativa


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        TUTOR = "TUTOR", "Tutor"
        VETERINÁRIO = "VETERINÁRIO", "Veterinário"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=100)
    celular = models.CharField(max_length=14, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.email

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return self.save(*args, **kwargs)

    class Meta:
        db_table = "users"


class VeterinarioManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.VETERINÁRIO)


class Veterinario(User):
    base_role = User.Role.VETERINÁRIO

    veterinario = VeterinarioManager()

    class Meta:
        proxy = True


class TutorManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.TUTOR)


class Tutor(User):
    base_role = User.Role.TUTOR

    tutor = TutorManager()

    class Meta:
        proxy = True
