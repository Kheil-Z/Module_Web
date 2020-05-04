from django import forms
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import Project

STATUS_CHOICES = [("n", "nouvelle"), ("enc", "en cours"), ("ena", "en attente"), ("t", "terminée"), ("cl", "classée")]


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class NewUserForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nom d'utilisateur", max_length=30)
    last_name = forms.CharField(label="Nom d'utilisateur", max_length=30)


class NewTaskForm(forms.Form):
    title = forms.CharField(label="Titre", max_length=100)
    description = forms.CharField(label="Description")
    start_date = forms.DateField(label="Date de début")
    due_date = forms.DateField(label="Date de fin")
    priority = forms.IntegerField(label="priorité")
    status = forms.ChoiceField(label="Status", choices=STATUS_CHOICES)
    project = forms.ModelChoiceField(label="Projet", queryset=Project.objects.all())
    assigned_to = forms.ModelChoiceField(label="Personne en charge", queryset=User.objects.all())

    def clean(self):

        # data from the form is fetched using super function
        super(NewTaskForm, self).clean()

        # extract the username and text field from the data
        priority = self.cleaned_data.priority('priority')
        start = self.cleaned_data.get('start_date')
        due = self.changed_data.get('due_date')

        # conditions to be met for the username length
        if (priority < 0) & (priority>10):
            self._errors['priority'] = self.error_class([
                'Priorite entre 0 et 11!'])
        if due < start:
            self._errors['due_date'] = self.error_class([
                'Votre date de fin est avant celle de début!'])
            self._errors['start_date'] = self.error_class([
                'Votre date de fin est avant celle de début!'])
            # return any errors if found
        return self.cleaned_data
