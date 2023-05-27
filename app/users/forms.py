from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from django import forms
from django.contrib.auth import get_user_model

from .models import User
from .models import Tutor
from .models import Veterinario


User = get_user_model()


class TutorSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    nome = forms.CharField(widget=forms.TextInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "password1", "password2")

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_tutor = True
        if commit:
            user.save()
        tutor = Tutor.objects.create(
            user=user,
            nome=self.cleaned_data.get("nome"),
        )
        return user


class VeterinarianSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    nome = forms.CharField(widget=forms.TextInput())
    nome_clinica = forms.CharField(widget=forms.TextInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "password1", "password2")

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_veterinarian = True
        if commit:
            user.save()
        veterinario = Veterinario.objects.create(
            user=user,
            nome=self.cleaned_data.get("nome"),
            nome_clinica=self.cleaned_data.get("nome_clinica"),
        )
        return user


class LoginForm(AuthenticationForm):
    email = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
