from django.urls import path

from .views import *

app_name = 'tutor'

urlpatterns = [
    path('list/', TutorListView.as_view(), name='tutor_list'),
    path('create/', TutorCreateView.as_view(), name='tutor_create'),
    path('detail/<pk>', TutorDetailView.as_view(), name='tutor_detail'),
    path('update/<pk>', TutorUpdateView.as_view(), name='tutor_update'),
    path('delete/<pk>', TutorDeleteView.as_view() , name='tutor_delete'),
]