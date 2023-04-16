from django.urls import path
from raca.views import *

app_name = 'raca'

urlpatterns = [
    path('list/', RacaListView.as_view(), name='raca_list'),
    path('create/', RacaCreateView.as_view(), name='raca_create'),
    path('detail/<pk>', RacaDetailView.as_view(), name='raca_detail'),
    path('update/<pk>', RacaUpdateView.as_view(), name='raca_update'),
    path('delete/<pk>', RacaDeleteView.as_view() , name='raca_delete'),
]
