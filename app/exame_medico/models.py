import uuid
from django.db import models
from django.urls import reverse

from pet.models import Pet
from users.models import Veterinario


class TipoExame(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, db_index=True, default=uuid.uuid4, editable=False
    )
    nome = models.CharField(max_length=100)

    class Meta:
        db_table = "tipo_exame"

    def __str__(self) -> str:
        return self.nome

    def get_absolute_url(self):
        return reverse("exame_medico:tipo_exame_detail", kwargs={"pk": self.id})


class ExameMedico(models.Model):
    FORMA_PAGAMENTO_CHOICES = [
        ("Dinheiro", "Dinheiro"),
        ("Cartão", "Cartão"),
        ("Pix", "Pix"),
    ]

    id = models.UUIDField(
        primary_key=True, unique=True, db_index=True, default=uuid.uuid4, editable=False
    )
    veterinario = models.ForeignKey(Veterinario, on_delete=models.PROTECT)
    pet = models.ForeignKey(Pet, on_delete=models.PROTECT)
    tipo_exame = models.ForeignKey(TipoExame, on_delete=models.PROTECT)
    # Imagens (máximo de 10)
    diagnostico = models.TextField(max_length=500)
    data_exame = models.DateField()
    forma_pagamento = models.CharField(
        max_length=8, choices=FORMA_PAGAMENTO_CHOICES, default="Cartão"
    )
    valor = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    class Meta:
        db_table = "exame_medico"

    def __str__(self) -> str:
        return (
            f"{self.data_exame} - {self.tipo_exame} - {self.veterinario} - {self.pet}"
        )

    def get_absolute_url(self):
        return reverse("exame_medico:exame_medico_detail", kwargs={"pk": self.id})
