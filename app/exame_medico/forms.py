from django import forms
from .models import ExameMedico


class ExameMedicoForm(forms.ModelForm):
    class Meta:
        model = ExameMedico
        fields = (
            "veterinario",
            "pet",
            "tipo_exame",
            "data_exame",
            "forma_pagamento",
            "valor",
            "diagnostico",
        )
