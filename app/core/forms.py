from django import forms

from app.core.models import Tutor

class TutorForm(forms.Model):
    class Meta:
        model = Tutor
        fields = '__all__'