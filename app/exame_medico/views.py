from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from exame_medico.forms import ExameMedicoForm

from exame_medico.models import ExameMedico, TipoExame


class TipoExameListView(LoginRequiredMixin, ListView):
    model = TipoExame
    fields = [
        "nome",
    ]
    context_object_name = "tipos_exames"
    template_name = "exame_medico/tipo_exame_list.html"


class TipoExameCreateView(LoginRequiredMixin, CreateView):
    model = TipoExame
    template_name = "exame_medico/tipo_exame_form.html"
    fields = [
        "nome",
    ]

    success_url = reverse_lazy("exame_medico:tipo-exame-list")


class TipoExameUpdateView(LoginRequiredMixin, UpdateView):
    model = TipoExame
    template_name = "exame_medico/tipo_exame_form.html"
    fields = [
        "nome",
    ]

    success_url = reverse_lazy("exame_medico:tipo-exame-list")


class TipoExameDetailView(LoginRequiredMixin, DetailView):
    model = TipoExame
    template_name = "exame_medico/tipo_exame_detail.html"


class TipoExameDeleteView(LoginRequiredMixin, DeleteView):
    model = TipoExame
    template_name = "exame_medico/tipo_exame_confirm_delete.html"

    success_url = reverse_lazy("users:veterinarian-home")

class ExameMedicoListView(LoginRequiredMixin, ListView):
    model = ExameMedico
    context_object_name = "exames_medicos"
    template_name = "exame_medico/exame_medico_list.html"


class ExameMedicoCreateView(LoginRequiredMixin, CreateView):
    model = ExameMedico
    form_class = ExameMedicoForm
    template_name = "exame_medico/exame_medico_form.html"

    success_url = reverse_lazy("exame_medico:exame-medico-list")


class ExameMedicoUpdateView(LoginRequiredMixin, UpdateView):
    model = ExameMedico
    form_class = ExameMedicoForm
    template_name = "exame_medico/exame_medico_form.html"

    success_url = reverse_lazy("exame_medico:exame-medico-list")


class ExameMedicoDetailView(LoginRequiredMixin, DetailView):
    model = ExameMedico


class ExameMedicoDeleteView(LoginRequiredMixin, DeleteView):
    model = ExameMedico

    success_url = reverse_lazy("exame_medico:exame-medico-list")
