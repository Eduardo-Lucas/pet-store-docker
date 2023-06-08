# import the required libraries
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.query import QuerySet
from django.utils import timezone
from django.urls import reverse
from core.choices import UnidadeFederativa


# class CustomUserManager(BaseUserManager):
#     def _create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError("Email deve ser informado.")
#         if not password:
#             raise ValueError("Senha deve ser informada.")

#         user = self.model(email=self.normalize_email(email), **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, password, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_active", True)
#         extra_fields.setdefault("is_superuser", False)
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_active", True)
#         extra_fields.setdefault("is_superuser", True)
#         return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        TUTOR = "TUTOR", "Tutor"
        VETERINÁRIO = "VETERINÁRIO", "Veterinário"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    email = models.EmailField(unique=True)

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

    nome = models.CharField(max_length=100)
    nome_clinica = models.CharField(max_length=100, null=True, blank=True)
    celular = models.CharField(max_length=14, null=True, blank=True)

    veterinario = VeterinarioManager()

    class Meta:
        proxy = True
        db_table = "veterinarios"

    def __str__(self) -> str:
        return self.nome


class TutorManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.TUTOR)


class Tutor(User):
    base_role = User.Role.TUTOR

    nome = models.CharField(max_length=100)
    celular = models.CharField(max_length=14, null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    rg = models.CharField(max_length=14, null=True, blank=True)
    rua = models.CharField(max_length=14, null=True, blank=True)
    numero = models.CharField(max_length=14, null=True, blank=True)
    complemento = models.CharField(max_length=14, null=True, blank=True)
    bairro = models.CharField(max_length=14, null=True, blank=True)
    cidade = models.CharField(max_length=14, null=True, blank=True)
    uf = models.CharField(
        max_length=14,
        null=True,
        blank=True,
        choices=UnidadeFederativa.choices,
        default="RJ",
    )
    observacao = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    tutor = TutorManager()

    class Meta:
        proxy = True
        db_table = "tutores"

    def __str__(self) -> str:
        return self.nome

    # @property
    # def quantidade_de_pets(self) -> int:
    #     qtd = Pet.objects.filter(tutor=self.id).count()
    #     return qtd

    # def __str__(self) -> str:
    #     if self.quantidade_de_pets == 0:
    #         return f'{self.nome} não possui nenhum pet cadastrado!'
    #     if self.quantidade_de_pets > 1:
    #         return f'{self.nome} possui {self.quantidade_de_pets} pets cadastrados!'
    #     else:
    #         return f'{self.nome} possui apenas {self.quantidade_de_pets} pet cadastrado'
