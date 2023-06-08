import uuid
from django.db import models
from django.urls import reverse

from smart_selects.db_fields import ChainedForeignKey

from core.choices import Sexo
from users.models import Tutor


class Especie(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome

    def get_absolute_url(self):
        return reverse("pet:especie_detail", kwargs={"pk": self.id})

    class Meta:
        ordering = ["nome"]
        db_table = "especie"


class Raca(models.Model):
    nome = models.CharField(max_length=100, unique=True, db_index=True)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)

    class Meta:
        db_table = "raca"

    def __str__(self) -> str:
        return self.nome

    def get_absolute_url(self):
        return reverse("pet:raca_detail", kwargs={"pk": self.id})


class Pet(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, db_index=True, default=uuid.uuid4, editable=False
    )
    tutor = models.ForeignKey(
        Tutor, db_index=True, on_delete=models.PROTECT, related_name="meu_dono"
    )
    nome = models.CharField(max_length=100)
    especie = models.ForeignKey(Especie, on_delete=models.PROTECT)

    raca = ChainedForeignKey(
        Raca,
        chained_field="especie",
        chained_model_field="especie",
        show_all=False,
        auto_choose=True,
        sort=True,
    )

    sexo = models.CharField(max_length=10, choices=Sexo.choices)
    idade = models.IntegerField(default=0)
    observacao = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nome} - Tutor: {self.tutor.nome}"

    class Meta:
        db_table = "pet"
