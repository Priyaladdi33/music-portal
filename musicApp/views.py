
from django.shortcuts import render
from .models import Song
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

@login_required(login_url='login')

def index(request):
    songs = Song.objects.all()  # Retrieve all songs from the database
    return render(request, 'musicApp/index.html', {'songs': songs})
# Filter Songs by Tag: Hindi (Requires login)
@login_required(login_url='login')
def hindi_songs(request):
    songs = Song.objects.filter(tags='Hindi')
    return render(request, 'musicApp/hindi.html', {'songs': songs})

# Filter Songs by Tag: Kannada (Requires login)
@login_required(login_url='login')
def kannada_songs(request):
    songs = Song.objects.filter(tags='Kannada')
    return render(request, 'musicApp/kannada.html', {'songs': songs})

# Filter Songs by Tag: English (Requires login)
@login_required(login_url='login')
def english_songs(request):
    songs = Song.objects.filter(tags='English')
    return render(request, 'musicApp/english.html', {'songs': songs})
