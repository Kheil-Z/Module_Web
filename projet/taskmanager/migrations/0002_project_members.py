# Generated by Django 2.1.15 on 2020-04-30 08:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='Members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
