import uuid
from django.db import models
from django.urls import reverse


from core.choices import Sexo
from users.models import Tutor


class Especie(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, db_index=True, default=uuid.uuid4, editable=False
    )
    nome = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome
    
    def get_absolute_url(self):
        return reverse("especie:especie_detail", kwargs={"pk": self.id})    

    
    class Meta:
        ordering = ["nome"]
        db_table = 'especie'


class Raca(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, db_index=True, default=uuid.uuid4, editable=False
    )
    nome = models.CharField(max_length=100, unique=True, db_index=True)

    class Meta:
        db_table = 'raca'

    def __str__(self) -> str:
        return self.nome
    
    def get_absolute_url(self):
        return reverse("raca:raca_detail", kwargs={"pk": self.id})    




class Pet(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, db_index=True, default=uuid.uuid4, editable=False
    )
    tutor = models.ForeignKey(
        Tutor, db_index=True, on_delete=models.PROTECT, related_name="meu_dono"
    )
    nome = models.CharField(max_length=100)
    raca = models.ForeignKey(Raca, on_delete=models.PROTECT)
    especie = models.ForeignKey(Especie, on_delete=models.PROTECT)
    sexo = models.CharField(max_length=10, choices=Sexo.choices)
    idade = models.IntegerField(default=0)
    observacao = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nome} - Tutor: {self.tutor.nome}"

    class Meta:
        db_table = "pet"
