import datetime

from django.shortcuts import render, get_object_or_404, redirect
from markdownx.utils import markdownify

from .forms import EventForm
from .forms import MemberForm
from .forms import RegionForm
from .forms import StoryForm
from .forms import TrackForm
from .models import Event
from .models import Member
from .models import Region
from .models import Story
from .models import Track


# Index page
def index(request):
    tracks = Track.objects.all()
    regions = Region.objects.all()

    now = datetime.datetime.now()
    last_event = Event.objects.filter(end_date__lt=now).order_by('-end_date').first()
    upcoming_event = Event.objects.filter(start_date__gt=now).order_by('start_date').first()
    last_stories = Story.objects.all().order_by('-create_date')[:5]
    params = {
        'regions': regions,
        'tracks': tracks,
        'last_event': last_event,
        'upcoming_event': upcoming_event,
        'last_stories': last_stories,
    }
    return render(request, 'ggit_platform/index.html', params)


# Admin index page
def admin_index(request):
    return redirect('region_list')


def track_detail(request, id):
    track = get_object_or_404(Track, id=id)
    track.markdown = markdownify(track.long_description)
    return render(request, 'track/detail.html', {'track': track})


# Track views
def track_list(request):
    tracks = Track.objects.all()
    return render(request, 'track/admin-list.html', {'tracks': tracks})


def track_new(request):
    if request.method == 'POST':
        form = TrackForm(request.POST)
        if form.is_valid():
            track = form.save()
            return redirect('track_list')
    elif request.method == 'GET':
        form = TrackForm()
    else:
        form = None
    return render(request, 'track/admin-edit.html', {'form': form})


def track_edit(request, id):
    track = get_object_or_404(Track, id=id)
    if request.method == 'GET':
        form = TrackForm(instance=track)
    elif request.method == 'POST':
        form = TrackForm(request.POST, instance=track)
        if form.is_valid():
            track = form.save()
            return redirect('track_list')
    else:
        form = None
    return render(request, 'track/admin-edit.html', {'form': form})


def track_delete(request, id):
    track = get_object_or_404(Track, id=id)
    if request.method == 'POST':
        track.delete()
    return redirect('track_list')


# Region views
def region_list(request):
    regions = Region.objects.all()
    return render(request, 'region/admin-list.html', {'regions': regions})


def region_detail(request, id):
    region = get_object_or_404(Region, id=id)
    events = Event.objects.filter(region=region).order_by('-start_date')[:3]
    stories = Story.objects.filter(region=region).order_by('-create_date')[:3]
    members = Member.objects.filter(region=region)
    params = {
        'region': region,
        'events': events,
        'stories': stories,
        'members': members
    }
    return render(request, 'region/detail.html', params)


def region_admin_detail(request, id):
    region = get_object_or_404(Region, id=id)
    return render(request, 'region/admin-detail.html', {'region': region})


def region_new(request):
    if request.method == 'POST':
        form = RegionForm(request.POST)
        if form.is_valid():
            region = form.save()
            return redirect('region_list')

    elif request.method == 'GET':
        form = RegionForm()
    else:
        form = None
    return render(request, 'region/admin-edit.html', {'form': form})


def region_edit(request, id):
    region = get_object_or_404(Region, id=id)
    if request.method == 'GET':
        form = RegionForm(instance=region)

    elif request.method == 'POST':
        form = RegionForm(request.POST, instance=region)
        if form.is_valid():
            region = form.save()
            return redirect('region_list')
    else:
        form = None
    return render(request, 'region/admin-edit.html', {'form': form})


def region_delete(request, id):
    region = get_object_or_404(Region, id=id)
    if request.method == 'POST':
        region.delete()
    return redirect('region_list')


# Member views
def member_list(request):
    members = Member.objects.all()
    return render(request, 'member/admin-list.html', {'members': members})


def member_new(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save()
            return redirect('member_list')
    elif request.method == 'GET':
        form = MemberForm()
    else:
        form = None
    return render(request, 'member/admin-edit.html', {'form': form})


def member_edit(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'GET':
        form = MemberForm(instance=member)
    elif request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            member = form.save()
            return redirect('member_list')
    else:
        form = None
    return render(request, 'member/admin-edit.html', {'form': form})


def member_delete(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        member.delete()
    return redirect('member_list')


# Event views
def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    event.markdown = markdownify(event.long_description)
    return render(request, 'event/detail.html', {'event': event})


def admin_event_list(request):
    events = Event.objects.all()
    return render(request, 'event/admin-list.html', {'events': events})


def admin_event_new(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return redirect('event_list')
    elif request.method == 'GET':
        form = EventForm()
    else:
        form = None
    return render(request, 'event/admin-edit.html', {'form': form})


def event_edit(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'GET':
        form = EventForm(instance=event)
    elif request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save()
            return redirect('event_list')
    else:
        form = None
    return render(request, 'event/admin-edit.html', {'form': form})


def event_delete(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        event.delete()
    return redirect('event_list')

def event_list(request):
    events = Event.objects.all()
    return render(request,'event/list.html', {'events': events})

# Story views
def story_list(request):
    stories = Story.objects.all()
    return render(request, 'story/admin-list.html', {'stories': stories})


def story_new(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save()
            return redirect('story_list')
    elif request.method == 'GET':
        form = StoryForm()
    else:
        form = None
    return render(request, 'story/admin-edit.html', {'form': form})


def story_edit(request, id):
    story = get_object_or_404(Story, id=id)
    if request.method == 'GET':
        form = StoryForm(instance=story)
    elif request.method == 'POST':
        form = StoryForm(request.POST, instance=story)
        if form.is_valid():
            story = form.save()
            return redirect('story_list')
    else:
        form = None
    return render(request, 'story/admin-edit.html', {'form': form})


def story_delete(request, id):
    story = get_object_or_404(Story, id=id)
    if request.method == 'POST':
        story.delete()
    return redirect('story_list')


def story_detail(request, id):
    story = get_object_or_404(Story, id=id)
    story.markdown = markdownify(story.long_description)
    return render(request, 'story/detail.html', {'story': story})
