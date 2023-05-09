from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from pet.models import Pet

class PetListView(ListView):
    model = Pet
    fields = [
        'nome',
    ]
    context_object_name = 'pets'
    template_name = 'pet:Pet_list.html'


class PetCreateView(CreateView):
    model = Pet
    fields = [
            'nome',
        ]
    

class PetDetailView(DetailView):
    model = Pet

class PetUpdateView(UpdateView):
    model = Pet
    fields = [
            'nome',
        ]

class PetDeleteView(DeleteView):
    model = Pet
    success_url = reverse_lazy('pet:pet_list')
