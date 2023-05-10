# import the required libraries
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.urls import reverse
from core.choices import UnidadeFederativa


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_veterinarian = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)

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

    def get_absolute_url(self):
        return reverse("veterinario:veterinario_detail", kwargs={"pk": self.id})


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

    def get_absolute_url(self):
        return reverse("tutor:tutor_detail", kwargs={"pk": self.id})

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
