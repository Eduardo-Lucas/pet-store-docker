from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_tutor = models.BooleanField(default=False)
    is_veterinario = models.BooleanField(default=False)

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
