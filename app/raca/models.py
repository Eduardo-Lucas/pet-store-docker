from django.db import models
from django.urls import reverse

import uuid

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

