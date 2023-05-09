import uuid
from django.db import models
# from especie.models import Especie
from raca.models import Raca

from core.choices import Sexo
from tutor.models import Tutor



class Pet(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, db_index=True, default=uuid.uuid4, editable=False
    )
    tutor = models.ForeignKey(Tutor, db_index=True, on_delete=models.PROTECT, 
                              related_name='meu_dono')
    nome = models.CharField(max_length=100)
    raca = models.ForeignKey(Raca, on_delete=models.PROTECT)
    # especie = models.ForeignKey(Especie, on_delete=models.PROTECT) 
    sexo = models.CharField(max_length=10, choices=Sexo.choices)
    idade = models.IntegerField(default=0)
    observacao = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.nome} - Tutor: {self.tutor.nome}'
    
    class Meta:
        db_table = 'pet'
