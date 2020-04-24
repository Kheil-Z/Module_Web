from django.db import models

class Track(models.Model):
    Name = models.CharField(max_length=200)
    Composer = models.CharField(max_length=220)
    Milliseconds = models.TextField(null=True)
    Bytes = models.IntegerField()

    UnitPrice = models.DecimalField(decimal_places=2, max_digits=5)

    album = models.ForeignKey('Album',on_delete=models.CASCADE)

class Artist(models.Model):
    Name = models.CharField(max_length=200)

class Album(models.Model):
    Title = models.CharField(max_length=200)
    artist = models.ForeignKey('Artist',on_delete=models.CASCADE)


# Create your models here.
