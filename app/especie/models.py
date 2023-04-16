from django.db import models
import uuid
from django.urls import reverse

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
