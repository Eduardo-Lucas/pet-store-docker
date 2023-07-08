from django.urls import path
from .views import *

app_name = "exame_medico"

urlpatterns = [
    ###############################################
    # Tipo de Exame
    ###############################################
    path("tipo-exame-list/", TipoExameListView.as_view(), name="tipo-exame-list"),
    path("tipo-exame-create/", TipoExameCreateView.as_view(), name="tipo-exame-create"),
    path(
        "tipo-exame-detail/<pk>",
        TipoExameDetailView.as_view(),
        name="tipo-exame-detail",
    ),
    path(
        "tipo-exame-update/<pk>",
        TipoExameUpdateView.as_view(),
        name="tipo-exame-update",
    ),
    path(
        "tipo-exame-delete/<pk>",
        TipoExameDeleteView.as_view(),
        name="tipo-exame-delete",
    ),
    ###############################################
    # Exame Médico
    ###############################################
    path("exame-medico-list/", ExameMedicoListView.as_view(), name="exame-medico-list"),
    path(
        "exame-medico-create/",
        ExameMedicoCreateView.as_view(),
        name="exame-medico-create",
    ),
    path(
        "exame-medico-detail/<pk>",
        ExameMedicoDetailView.as_view(),
        name="exame-medico-detail",
    ),
    path(
        "exame-medico-update/<pk>",
        ExameMedicoUpdateView.as_view(),
        name="exame-medico-update",
    ),
    path(
        "exame-medico-delete/<pk>",
        ExameMedicoDeleteView.as_view(),
        name="exame-medico-delete",
    ),
]
