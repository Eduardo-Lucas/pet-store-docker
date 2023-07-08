from django import forms
from .models import Pet, Raca


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ("nome", "especie", "raca", "sexo", "idade", "observacao")
