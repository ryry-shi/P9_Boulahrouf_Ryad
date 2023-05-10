from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import RegisterForm


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "core/register.html", {"form": form})


def home_view(request):
    return render(request, "core/home.html", {"user": request.user})


def logout_view(request):
    logout(request)
    return redirect("login")


def login_view(request):
    # si utilisateur est déja connecter on le redirige vers home
    if request.user.is_authenticated:
        return redirect("ticketing:flux")
    # si elle est en mode POST alors l'utilisateur alors a remplis le formulaire et on l'authentifie
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        # On vérifie si le formulaire est valide et si est le valide on authentifie la personne d'aprés les données du formulaire
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            # Si on réussi a l'authentifier on le connecte
            if user is not None:
                login(request, user)
                messages.info(request, "Vous êtes bien connectés")
                return redirect("ticketing:flux")
            else:
                return redirect("login")
    # si la requète est en mode get alors on affiche la page avec un formulaire vide
    else:
        form = AuthenticationForm()
    return render(request, "core/login.html", {"form": form})


def index_view(request):
    if request.user.is_authenticated:
        return redirect("ticketing:flux")
    return redirect("login")
