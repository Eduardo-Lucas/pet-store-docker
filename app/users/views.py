from django.shortcuts import redirect, render
from django.views.generic import CreateView


from pet.models import Pet
from exame_medico.models import ExameMedico
from .models import User
from .forms import TutorSignUpForm, VeterinarianSignUpForm, LoginForm
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .decorators import tutor_required, veterinario_required


class TutorSignUpView(CreateView):
    model = User
    form_class = TutorSignUpForm
    template_name = "users/tutor_signup.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "tutor"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("users:tutor-home")


class VeterinarianSignUpView(CreateView):
    model = User
    form_class = VeterinarianSignUpForm
    template_name = "users/veterinarian_signup.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "veterinarian"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("users:veterinarian-home")


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = "users/login.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_tutor:
                return reverse("users:tutor-home")
            elif user.is_veterinario:
                return reverse("users:veterinarian-home")
        else:
            return reverse("users:login")


class LogoutView(auth_views.LogoutView):
    template_name = "users/logout.html"


@login_required
@tutor_required
def tutor_home(request):
    # context = {"pets": Pet.objects.filter(tutor=request.user.tutor).order_by("nome")}
    return render(request, "users/tutor_home.html", {})


@login_required
@veterinario_required
def veterinarian_home(request):
    # context = {
    #     "exames_medicos": ExameMedico.objects.filter(
    #         veterinario=request.user.veterinario
    #     )
    # }
    return render(request, "users/veterinarian_home.html", {})
