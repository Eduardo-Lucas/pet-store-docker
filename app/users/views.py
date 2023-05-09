from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .models import User
from .forms import TutorSignUpForm, VeterinarianSignUpForm, LoginForm
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .decorators import tutor_required, veterinarian_required


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
        return redirect("tutor-home")


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
        return redirect("veterinarian-home")


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = "users/login.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_tutor:
                return reverse("tutor-home")
            elif user.is_veterinarian:
                return reverse("veterinarian-home")
        else:
            return reverse("login")


@login_required
@tutor_required
def tutor_home(request):
    context = {"questions": "Wlecome to Tutor's Home"}
    return render(request, "users/tutor_home.html", context)


@login_required
@veterinarian_required
def veterinarian_home(request):
    context = {"questions": "Welcome to Veterinarian's Home"}
    return render(request, "users/veterinarian_home.html", context)
