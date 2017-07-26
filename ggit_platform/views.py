from django.shortcuts import render, get_object_or_404

from .models import Track
from .models import Member
from .models import Region

# Track views
def tracks_list(request):
    tracks = Track.objects.all()

    return render(request, 'track/list.html', {'tracks': tracks})


def track_detail(request, id):
    track = get_object_or_404(Track, id=id)

    return render(request, 'track/detail.html', {'track': track})


# Region views
def region_list(request):
    regions = Region.objects.all()

    return render(request, 'region/list.html', {'regions': regions})

# Member views
def member_list(request):
    members = Member.objects.all()

    return render(request, 'member/list.html', {'members': members})

# Event views


# Story views
