from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from raca.models import Raca

class RacaListView(ListView):
    model = Raca
    fields = [
        'nome',
    ]
    context_object_name = 'racas'
    template_name = 'raca:raca_list.html'


class RacaCreateView(CreateView):
    model = Raca
    fields = [
            'nome',
        ]
    

class RacaDetailView(DetailView):
    model = Raca

class RacaUpdateView(UpdateView):
    model = Raca
    fields = [
            'nome',
        ]

class RacaDeleteView(DeleteView):
    model = Raca
    success_url = reverse_lazy('raca:raca_list')
