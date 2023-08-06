from django.shortcuts import redirect, render
from django.views.generic import CreateView


from pet.models import Pet
from exame_medico.models import ExameMedico
from .models import User
from .forms import TutorSignUpForm, VeterinarianSignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .decorators import tutor_required, veterinario_required
from django.contrib import messages
from django.views import View


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


class VeterinarianSignUpView(View):
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


class LoginView(View):
    form_class = LoginForm
    template_name = "users/login.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={"form": form})

    def post(self, request):
        form = self.form_class(request.POST)

        username = request.POST["username"]
        print("USERNAME: ", username)
        password = request.POST["password"]
        print("PASSWORD: ", password)

        user = authenticate(request, username=username, password=password)
        messages.success(request, "Authenticated successfully")
        if user is not None:
            login(request, user)
            messages.info(request, "Redirected to Home page")
            if user.is_tutor:
                return redirect("users:tutor-home")
            elif user.is_veterinario:
                return redirect("users:veterinarian-home")
            
            messages.success(request,"")
            messages.info(request,"")

        else:
            messages.error(request, "Invalid username or password")

        return render(request, self.template_name, context={"form": form})


class LogoutView(LogoutView):
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
