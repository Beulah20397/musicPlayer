from django.http import Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Album, Song

def index(request) :

    all_albums  = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        "all_albums" : all_albums
    }
    html = ''
    return render(request, 'music/index.html', context)

def detail(request, album_id) :
    # instead of try catch use get_objecct_or_404
    album  = get_object_or_404(Album, pk=album_id) 
    return render(request, 'music/detail.html', {"album": album})

def favorite(request,album_id) :
    album  = get_object_or_404(Album, pk=album_id)
    try :
        selectedSong = album.song_set.get(pk=request.POST['song'])
    except (KeyError, SongDoesNotExists) :
        return render(request, 'music/detail.html',{
            "album" : album,
            error_message : "You did not select a valid song"
        })
    else : 
        selectedSong.is_favorite = True
        selectedSong.save()
        return render(request, 'music/detail.html', {"album": album})
