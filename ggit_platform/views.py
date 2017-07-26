from django.shortcuts import render, get_object_or_404

from .models import Track
from .models import Member
from .models import Region
from .models import Event
from .models import Story

# Index page
def index(request):
    return render(request, 'ggit_platform/index.html')

# Track views
def track_list(request):
    tracks = Track.objects.all()

    return render(request, 'track/list.html', {'tracks': tracks})


def track_detail(request, id):
    track = get_object_or_404(Track, id=id)

    return render(request, 'track/detail.html', {'track': track})


# Region views
def region_list(request):
    regions = Region.objects.all()

    return render(request, 'region/list.html', {'regions': regions})

def region_detail(request, id):
    region = get_object_or_404(Region, id=id)
    return render(request, 'region/detail.html', {'region' : region})

# Member views
def member_list(request):
    members = Member.objects.all()

    return render(request, 'member/list.html', {'members': members})

def member_details(request, id):
    member = get_object_or_404(Member, id=id)

    return render(request, 'member/details.html', {'member': member})

# Event views
def event_list(request):
    events= Event.objects.all()
    return render (request, 'event/list.html', {'events':events})


# Story views
def stories_list(request):
    stories = Story.objects.all()

    return render(request, 'story/list.html', {'stories': stories})

def stories_detail(request, id):
    story = get_object_or_404(Story, id=id)

    return render(request, 'story/detail.html', {'story':story})
