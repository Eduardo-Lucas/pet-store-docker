from django.urls import path
from especie.views import *

app_name = 'especie'

urlpatterns = [
    path('list/', EspecieListView.as_view(), name='especie_list'),
    path('create/', EspecieCreateView.as_view(), name='especie_create'),
    path('detail/<pk>', EspecieDetailView.as_view(), name='especie_detail'),
    path('update/<pk>', EspecieUpdateView.as_view(), name='especie_update'),
    path('delete/<pk>', EspecieDeleteView.as_view() , name='especie_delete'),
]
