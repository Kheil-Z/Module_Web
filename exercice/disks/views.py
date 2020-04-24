from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .forms import QueryForm
from .models import Album, Track


def home(request):
    albums = Album.objects.all()
    return render(request, 'disks/home.html', {'all_album': albums})


def album(request, id):
    album = get_object_or_404(Album, id=id)
    albums = Album.objects.all()
    tracks = Track.objects.filter(album=album)
    return render(request, 'disks/album.html', {'album': album, 'all_album': albums, 'tracks': tracks})


def query(request):
    if request.GET:
        query = request.GET['q']
        q_str = str(query)

    albums =[]
    queries = q_str.split()
    for q in queries:
        alb = Album.objects.filter(Q(Title__contains=q))
        for album in alb:
            albums.append(album)
    return render(request,'disks/query.html', {'albums':albums})

