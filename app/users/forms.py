# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.db import transaction
# from django import forms
# from django.contrib.auth import get_user_model

# from .models import User
# from .models import Tutor
# from .models import Veterinario


# User = get_user_model()


# class TutorSignUpForm(UserCreationForm):
#     email = forms.EmailField(widget=forms.EmailInput())
#     password1 = forms.CharField(widget=forms.PasswordInput())
#     password2 = forms.CharField(widget=forms.PasswordInput())


#     class Meta(UserCreationForm.Meta):
#         model = Tutor
#         fields = ("email", "password1", "password2")

#     @transaction.atomic
#     def save(self, commit=True):
#         tutor = super().save(commit=False)
#         if commit:
#             tutor.save()
#         tutor = Tutor.objects.create(
#             tutor=tutor,
#             nome=self.cleaned_data.get("nome"),
#         )
#         return tutor


# class VeterinarianSignUpForm(UserCreationForm):
#     email = forms.EmailField(widget=forms.EmailInput())
#     password1 = forms.CharField(widget=forms.PasswordInput())
#     password2 = forms.CharField(widget=forms.PasswordInput())

#     nome = forms.CharField(widget=forms.TextInput())
#     nome_clinica = forms.CharField(widget=forms.TextInput())

#     class Meta(UserCreationForm.Meta):
#         model = Veterinario
#         fields = ("email", "password1", "password2")

#     @transaction.atomic
#     def save(self, commit=True):
#         veterinario = super().save(commit=False)
#         if commit:
#             veterinario.save()
#         veterinario = Veterinario.objects.create(
#             veterinario=veterinario,
#             nome=self.cleaned_data.get("nome"),
#             nome_clinica=self.cleaned_data.get("nome_clinica"),
#         )
#         return veterinario


# class LoginForm(AuthenticationForm):
#     email = forms.CharField(widget=forms.TextInput())
#     password = forms.CharField(widget=forms.PasswordInput())
