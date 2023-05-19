from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from pet.models import Pet, Raca
from pet.forms import PetForm


def load_racas(request):
    especie_id = request.GET.get('especie')
    racas = Raca.objects.filter(especie_id=especie_id).order_by('nome')
    return render(request, 'pet/dropdown_list.html', {'racas': racas})

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


class PetDetailView(DetailView):
    model = Pet


class PetUpdateView(UpdateView):
    model = Pet
    fields = [
        "nome",
    ]


class PetDeleteView(DeleteView):
    model = Pet
    success_url = reverse_lazy("pet:pet_list")


class RacaCreateView(CreateView):
    model = Raca
    template_name = "pet/raca_form.html"
    fields = [
        "nome",
    ]


class RacaDetailView(DetailView):
    model = Raca
