from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

#Variable pour le choix des status
STATUS_CHOICES = [("n", "nouvelle"), ("enc", "en cours"), ("ena", "en attente"), ("t", "terminée"), ("cl", "classée")]


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    start_date = models.DateField()
    due_date = models.DateField()
    priority = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(10), MinValueValidator(0)],
    )
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    #Pour pouvoir afficher correctement le status de la tache
    def status(self):
        if self.status == "n":
            return ("nouvelle")
        elif self.status == "enc":
            return ("en cours")
        elif self.status == "ena":
            return ("en attente")
        else:
            return ("classée")


class Comment(models.Model):
    message = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.message


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.title