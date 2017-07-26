from django.shortcuts import render, get_object_or_404

from .models import Track

# Track views
def tracks_list(request):
    tracks = Track.objects.all()

    return render(request, 'track/list.html', {'tracks': tracks})


def track_detail(request, id):
    track = get_object_or_404(Track, id=id)

    return render(request, 'track/detail.html', {'track': track})


# Region views


# Member views


# Event views


# Story views
