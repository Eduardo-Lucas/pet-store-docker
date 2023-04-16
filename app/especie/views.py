from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from especie.models import Especie

class EspecieListView(ListView):
    model = Especie
    fields = [
        'nome',
    ]
    context_object_name = 'especies'
    template_name = 'especie:especie_list.html'


class EspecieCreateView(CreateView):
    model = Especie
    fields = [
            'nome',
        ]
    

class EspecieDetailView(DetailView):
    model = Especie

class EspecieUpdateView(UpdateView):
    model = Especie
    fields = [
            'nome',
        ]

class EspecieDeleteView(DeleteView):
    model = Especie
    success_url = reverse_lazy('especie:especie_list')
