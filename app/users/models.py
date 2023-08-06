from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError("Password must be provided")

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
    username = None
    email = models.EmailField(unique=True)
    is_tutor = models.BooleanField(default=False)
    is_veterinario = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Tutor(models.Model):
    user = models.OneToOneField(
        User,
        related_name="tutors",
        on_delete=models.CASCADE,
        primary_key=True,
    )
    nome = models.CharField(max_length=50)
    celular = models.CharField(max_length=11, blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    rg = models.CharField(max_length=11, blank=True, null=True)
    rua = models.CharField(max_length=50, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    complemento = models.CharField(max_length=20, blank=True, null=True)
    bairro = models.CharField(max_length=15, blank=True, null=True)
    cidade = models.CharField(max_length=20, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    observacao = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("nome",)

    def __str__(self) -> str:
        return self.nome


class Veterinario(models.Model):
    user = models.OneToOneField(
        User,
        related_name="veterinarios",
        on_delete=models.CASCADE,
        primary_key=True,
    )
    nome = models.CharField(max_length=50)
    nome_clinica = models.CharField(max_length=50)
    celular = models.CharField(max_length=11, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("nome",)

    def __str__(self) -> str:
        return self.nome
