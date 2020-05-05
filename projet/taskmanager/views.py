from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import ConnexionForm, NewUserForm, NewTaskForm, NewProjectForm
from .models import Project, Task, Comment


def home(request): # Page D'acceuille
    if request.user.is_authenticated: #Si l'utilisateur est connectee on receuille ses donnees, qui passeront a la vue
        user = request.user
        projects = Project.objects.filter(members=user)
    return render(request, 'taskmanager/home.html', locals())


def connexion(request): #Fonction de connexion basic
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
    if request.user.is_authenticated:
        user = request.user
        projects = Project.objects.filter(members=user)
    return render(request, 'taskmanager/connexion.html', locals())



def createnewUser(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            user.save()
            return render(request, 'taskmanager/home.html')
    else :
        form = NewUserForm()
        return render(request, 'taskmanager/newuser.html', {"form": form})


def deconnexion(request):
    logout(request)
    return render(request, 'taskmanager/logout.html')


@login_required
def task(request, id1, id2):
    projects = Project.objects.all()
    project = projects.get(id=id1)
    tasks = Task.objects.filter(project=project)
    task = tasks.get(id=id2)
    comments = Comment.objects.filter(task=task).order_by('-date')
    return render(request, 'taskmanager/task.html',locals())
                 # {"comments": comments, "projects": projects, "project": project, "tasks": tasks, "task": task})


@login_required
def project(request, id):
    user = request.user
    projects = Project.objects.all()
    project = projects.get(id=id)
    tasks = Task.objects.filter(project=project)
    return render(request, 'taskmanager/project.html',
                  {"user": user, "projects": projects, "project": project, "tasks": tasks})


@login_required
def projects(request):
    user = request.user
    projects = Project.objects.all()
    return render(request, 'taskmanager/projects.html', {"user": user, "projects": projects})


@login_required
def createnewTask(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST or None)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            start_date = form.cleaned_data["start_date"]
            due_date = form.cleaned_data["due_date"]
            priority = form.cleaned_data["priority"]
            assigned_to = form.cleaned_data["assigned_to"]
            status = form.cleaned_data["status"]
            project = form.cleaned_data["project"]
            task = Task.objects.create(title=title, description=description, start_date=start_date, due_date=due_date,
                                       priority=priority, assigned_to=assigned_to, project=project)
            task.status=status
            task.save()
            project.members.add(assigned_to)
            project.save()
            return redirect('/taskmanager/projects')
        else:
            form = NewTaskForm()
            return render(request, 'taskmanager/newtask.html', locals())
    else :
        form = NewTaskForm();
        return render(request, 'taskmanager/newtask.html', {"form": form})

@login_required
def editTask(request,id1,id2):
    if request.method == "POST":
        form = NewTaskForm(request.POST or None)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            start_date = form.cleaned_data["start_date"]
            due_date = form.cleaned_data["due_date"]
            priority = form.cleaned_data["priority"]
            assigned_to = form.cleaned_data["assigned_to"]
            status = form.cleaned_data["status"]
            project = form.cleaned_data["project"]

            task = Task.objects.get(id=id2)
            task.title = title
            task.description =description
            task.start_date = start_date
            task.due_date = due_date
            task.priority = priority
            task.assigned_to = assigned_to
            task.status = status
            task.project = project
            task.save()

            project.members.add(assigned_to)
            project.save()
            return redirect('/taskmanager/project/'+str(id1))
        else:
            form = NewTaskForm()
            return render(request, 'taskmanager/newtask.html', locals())
    else:
        instance = Task.objects.get(id=id2)
        form = NewTaskForm(initial={'title':instance.title,'description':instance.description,
                                    'start_date':instance.start_date,'due_date':instance.due_date,
                                    'priority':instance.priority, 'assigned_to':instance.assigned_to,
                                    'status':instance.status, 'project':instance.project})
        return render(request, 'taskmanager/edittask.html',locals())

@login_required
def createnewProject(request):
    if request.method == "POST":
        form = NewProjectForm(request.POST or None)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            members = form.cleaned_data["members"]

            project = Task.objects.create(title=title, description=description,members=members)

            project.save()
            return redirect('/taskmanager/projects')
        else:
            form = NewProjectForm()
            return render(request, 'taskmanager/newproject.html', locals())
    else :
        form = NewProjectForm();
        return render(request, 'taskmanager/newproject.html', {"form": form})