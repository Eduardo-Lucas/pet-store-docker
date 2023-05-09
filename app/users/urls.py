from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.tutor_home, name="tutor-home"),
    path("veterinarian/", views.veterinarian_home, name="veterinarian-home"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/tutor/", views.TutorSignUpView.as_view(), name="tutor-signup"),
    path("signup/veterinarian/", views.VeterinarianSignUpView.as_view(), name="veterinarian-signup"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
        
]
