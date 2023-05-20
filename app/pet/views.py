from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from pet.models import Pet, Raca
from pet.forms import PetForm


class PetListView(LoginRequiredMixin, ListView):
    model = Pet
    fields = [
        "nome",
    ]
    context_object_name = "pets"
    template_name = "pet/pet_list.html"


class PetCreateView(LoginRequiredMixin, CreateView):
    model = Pet
    template_name = "pet/pet_form.html"
    form_class = PetForm

    success_url = reverse_lazy('users:tutor-home')

    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.tutor = self.request.user.tutor
        pet.save()
        return super(PetCreateView, self).form_valid(form)


class PetDetailView(LoginRequiredMixin, DetailView):
    model = Pet


class PetUpdateView(LoginRequiredMixin, UpdateView):
    model = Pet
    template_name = "pet/pet_form.html"
    form_class = PetForm

    success_url = reverse_lazy("users:tutor-home")

class PetDeleteView(LoginRequiredMixin, DeleteView):
    model = Pet
    success_url = reverse_lazy("users:tutor-home")


class RacaCreateView(LoginRequiredMixin, CreateView):
    model = Raca
    template_name = "pet/raca_form.html"
    fields = [
        "nome",
    ]


class RacaDetailView(LoginRequiredMixin, DetailView):
    model = Raca
