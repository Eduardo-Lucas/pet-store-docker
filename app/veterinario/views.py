from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from veterinario.models import Veterinario


class VeterinarioListView(ListView):
    model = Veterinario
    fields = '__all__'
    context_object_name = 'veterinarios'
    template_name = 'veterinario_list.html'


class VeterinarioCreateView(CreateView):
    model = Veterinario
    fields = [
            'nome',
            'nome_clinica',
            'email',
            'celular',
    ]
    

class VeterinarioDetailView(DetailView):
    model = Veterinario


class VeterinarioUpdateView(UpdateView):
    model = Veterinario
    fields = fields = [
            'nome',
            'nome_clinica',
            'email',
            'celular',
    ]


class VeterinarioDeleteView(DeleteView):
    model = Veterinario
    success_url = reverse_lazy('veterinario:veterinario_list')
