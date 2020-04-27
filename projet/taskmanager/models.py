from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    start_date = models.DateField()
    due_date = models.DateField()
    priority = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(10), MinValueValidator(0)]
    )
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(null=False)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)


class Project(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField(null=True)

# Create your models here.
