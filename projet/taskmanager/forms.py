from django import forms
from django.contrib.auth.models import User
from django.forms import DateInput, SelectDateWidget

from .models import Project, Task

#Encore, il nous faut cette liste pour choisir parmis les status possible
STATUS_CHOICES = [("n", "nouvelle"), ("enc", "en cours"), ("ena", "en attente"), ("t", "terminée"), ("cl", "classée")]

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class NewUserForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Prenom", max_length=30)
    last_name = forms.CharField(label="Nom", max_length=30)


class NewTaskForm(forms.Form):

    title = forms.CharField(label="Titre", max_length=100)
    description = forms.CharField(label="Description", widget=forms.Textarea)
    start_date = forms.DateField(label="Date de début", widget=SelectDateWidget())
    due_date = forms.DateField(label="Date de fin", widget=SelectDateWidget())
    priority = forms.IntegerField(label="priorité")
    status = forms.ChoiceField(label="Status", choices=STATUS_CHOICES)
    project = forms.ModelChoiceField(label="Projet", queryset=Project.objects.all())
    assigned_to = forms.ModelChoiceField(label="Personne en charge", queryset=User.objects.all())

    # Fonction pour valider correctement le formulaire
    def clean(self):
        # data from the form is fetched using super function
        cleaned_data = super(NewTaskForm, self).clean()
        # extract the username and text field from the data
        priority = self.cleaned_data['priority']
        start = self.cleaned_data['start_date']
        due = self.cleaned_data['due_date']

        # conditions to be met for the username length
        if (priority < 0) or (priority > 10):
            self.add_error("priority", "Priorité entre 0 et 10!")
        if due < start:
            self.add_error("due_date", "Date de début devrait etre avant celle de fin!")
            # return any errors if found
        return cleaned_data

class NewProjectForm(forms.Form):
    title = forms.CharField(label="Titre", max_length=100)
    description = forms.CharField(label="Description", widget=forms.Textarea)
    members = forms.ModelMultipleChoiceField(label="Participants",queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple)


class NewCommentForm(forms.Form):
    message = forms.CharField(label="Message", widget=forms.Textarea)



