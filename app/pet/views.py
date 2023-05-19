from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy, reverse

from pet.models import Pet, Raca
from pet.forms import PetForm


class PetListView(ListView):
    model = Pet
    fields = [
        "nome",
    ]
    context_object_name = "pets"
    template_name = "pet/pet_list.html"


class PetCreateView(CreateView):
    model = Pet
    template_name = "pet/pet_form.html"
    form_class = PetForm

    success_url = reverse_lazy('users:tutor-home')

    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.tutor = self.request.user.tutor
        pet.save()
        return super(PetCreateView, self).form_valid(form)


class PetDetailView(DetailView):
    model = Pet


class PetUpdateView(UpdateView):
    model = Pet
    template_name = "pet/pet_form.html"
    form_class = PetForm

    success_url = reverse_lazy("users:tutor-home")

class PetDeleteView(DeleteView):
    model = Pet
    success_url = reverse_lazy("users:tutor-home")


class RacaCreateView(CreateView):
    model = Raca
    template_name = "pet/raca_form.html"
    fields = [
        "nome",
    ]


class RacaDetailView(DetailView):
    model = Raca
