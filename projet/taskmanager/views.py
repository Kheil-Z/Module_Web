from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import ConnexionForm, NewUserForm
from .models import Project


def home(request):
    user =request.user
    projects = Project.objects.filter(members=user)
    return render(request, 'taskmanager/home.html',{"user": user, "projects": projects} )


def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else:  # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()
    return render(request, 'taskmanager/connexion.html', locals())

def newUser(request):
    form = NewUserForm();
    return render(request, 'taskmanager/newuser.html', {"form":form})

def createnewUser(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password)
            user.save()
    return  render(request, 'taskmanager/home.html')


def deconnexion(request):
    logout(request)
    return render(request, 'taskmanager/logout.html')


@login_required
def tasks(request):
    user = request.user
    projects = Project.objects.filter(members=user)
    return render(request, 'taskmanager/tasks.html', {"user": user, "projects": projects})
