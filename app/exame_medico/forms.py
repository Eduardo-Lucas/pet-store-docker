from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput
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
        widgets = {
            "data_exame": DatePickerInput(options={"format": "DD/MM/YYYY"}),
        }