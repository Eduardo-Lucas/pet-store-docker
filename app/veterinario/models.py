from django.utils import timezone
from django.db import models
from django.urls import reverse
import uuid

from users.models import User


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
