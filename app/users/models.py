# import the required libraries
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
from django.urls import reverse
from core.choices import UnidadeFederativa


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email deve ser informado.")
        if not password:
            raise ValueError("Senha deve ser informada.")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    is_veterinarian = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email

    class Meta:
        db_table = "users"


class Veterinario(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, db_index=True, default=uuid.uuid4, editable=False
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=False,
        unique=True,
        related_name="veterinario",
    )
    nome = models.CharField(max_length=100)
    nome_clinica = models.CharField(max_length=100, null=True, blank=True)
    celular = models.CharField(max_length=14, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "veterinarios"

    def __str__(self) -> str:
        return self.nome


class Tutor(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, db_index=True, default=uuid.uuid4, editable=False
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=False,
        unique=True,
        related_name="tutor",
    )
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

    class Meta:
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
