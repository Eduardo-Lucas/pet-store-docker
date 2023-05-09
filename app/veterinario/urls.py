from django.urls import path

from .views import *

app_name = 'veterinario'

urlpatterns = [
    path('list/', VeterinarioListView.as_view(), name='veterinario_list'),
    path('create/', VeterinarioCreateView.as_view(), name='veterinario_create'),
    path('detail/<pk>', VeterinarioDetailView.as_view(), name='veterinario_detail'),
    path('update/<pk>', VeterinarioUpdateView.as_view(), name='veterinario_update'),
    path('delete/<pk>', VeterinarioDeleteView.as_view() , name='veterinario_delete'),
]