from django.urls import path
from .views import *

app_name = 'pet'

urlpatterns = [
    path('list/', PetListView.as_view(), name='pet_list'),
    path('create/', PetCreateView.as_view(), name='pet_create'),
    path('detail/<pk>', PetDetailView.as_view(), name='pet_detail'),
    path('update/<pk>', PetUpdateView.as_view(), name='pet_update'),
    path('delete/<pk>', PetDeleteView.as_view() , name='pet_delete'),

    path('raca_create/', RacaCreateView.as_view(), name='raca_create'),
    path('raca_detail/<pk>', RacaDetailView.as_view(), name='raca_detail'),
    
]