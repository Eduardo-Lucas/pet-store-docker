from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from tutor.forms import TutorForm

from tutor.models import Tutor


class TutorListView(ListView):
    model = Tutor
    fields = '__all__'
    context_object_name = 'tutores'
    template_name = 'tutor_list.html'


class TutorCreateView(CreateView):
    model = Tutor
    fields = [
            'nome',
            'celular',
            'cpf',
            'rg',
            'rua',
            'numero',
            'complemento',
            'bairro',
            'cidade',
            'uf',
            'email',
            'observacao',
        ]
    

class TutorDetailView(DetailView):
    model = Tutor

class TutorUpdateView(UpdateView):
    model = Tutor
    fields = [
            'nome',
            'celular',
            'cpf',
            'rg',
            'rua',
            'numero',
            'complemento',
            'bairro',
            'cidade',
            'uf',
            'email',
            'observacao',
        ]

class TutorDeleteView(DeleteView):
    model = Tutor
    success_url = reverse_lazy('tutor:tutor_list')