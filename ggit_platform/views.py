from django.shortcuts import render, get_object_or_404, redirect

from .models import Track
from .models import Member
from .models import Region
from .models import Event
from .models import Story

from .forms import TrackForm
from .forms import MemberForm
from .forms import EventForm
from .forms import StoryForm
from .forms import RegionForm


# Index page
def index(request):
    return render(request, 'ggit_platform/index.html', {})
    

# Index page
def admin_index(request):
    return redirect('region_list')

# Track views
def track_list(request):
    tracks = Track.objects.all()
    return render(request, 'track/list.html', {'tracks': tracks})


def track_new(request):
    if request.method == 'POST':
        form = TrackForm(request.POST)
        if form.is_valid():
            track = form.save()
            return redirect('track_list')

    elif request.method == 'GET':
        form = TrackForm()
    return render(request, 'track/edit.html', {'form': form})


def track_edit(request, id):
    track = get_object_or_404(Track, id=id)
    if request.method == 'GET':
        form = TrackForm(instance=track)

    elif request.method == 'POST':
        form = TrackForm(request.POST, instance=track)
        if form.is_valid():
            track = form.save()
            return redirect('track_list')

    return render(request, 'track/edit.html', {'form': form})


def track_delete(request, id):
    track = get_object_or_404(Track, id=id)
    if request.method == 'POST':
        track.delete()

    return redirect('track_list')


# Region views
def region_list(request):
    regions = Region.objects.all()
    return render(request, 'region/list.html', {'regions': regions})

def region_detail(request, id):
    region = get_object_or_404(Region, id=id)
    return render(request, 'region/detail.html', {'region' : region})

def region_new(request):
    if request.method == 'POST':
        form = RegionForm(request.POST)
        if form.is_valid():
            region = form.save()
            return redirect('region_list')

    elif request.method == 'GET':
        form = RegionForm()
    return render(request, 'region/edit.html', {'form': form})


def region_edit(request, id):
    region = get_object_or_404(Region, id=id)
    if request.method == 'GET':
        form = RegionForm(instance=region)

    elif request.method == 'POST':
        form = RegionForm(request.POST, instance=region)
        if form.is_valid():
            region = form.save()
            return redirect('region_list')

    return render(request, 'region/edit.html', {'form': form})


def region_delete(request, id):
    region = get_object_or_404(Region, id=id)
    if request.method == 'POST':
        region.delete()

    return redirect('region_list')

# Member views
def member_list(request):
    members = Member.objects.all()
    return render(request, 'member/list.html', {'members': members})

def member_detail(request, id):
    member = get_object_or_404(Member, id=id)
    return render(request, 'member/detail.html', {'member': member})

def member_new(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save()
            return redirect('member_list')

    elif request.method == 'GET':
        form = MemberForm()
    return render(request, 'member/edit.html', {'form': form})


def member_edit(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'GET':
        form = MemberForm(instance=member)

    elif request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            member = form.save()
            return redirect('member_list')

    return render(request, 'member/edit.html', {'form': form})


def member_delete(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        member.delete()

    return redirect('member_list')

# Event views


def event_list(request):
    events= Event.objects.all()
    return render(request, 'event/list.html', {'events':events})


def event_new(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return redirect('event_list')

    elif request.method == 'GET':
        form = EventForm()
    return render(request, 'event/edit.html', {'form': form})

def event_edit(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'GET':
        form = EventForm(instance=event)

    elif request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save()
            return redirect('event_list')

    return render(request, 'event/edit.html', {'form': form})

def event_delete(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        event.delete()
    return redirect('event_list')

# Story views
def story_list(request):
    stories = Story.objects.all()
    return render(request, 'story/list.html', {'stories': stories})

def story_new(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save()
            return redirect('story_list')

    elif request.method == 'GET':
        form = StoryForm()
        
    return render(request, 'story/edit.html', {'form': form})

def story_edit(request, id):
    story = get_object_or_404(Story, id=id)
    if request.method == 'GET':
        form = StoryForm(instance=story)

    elif request.method == 'POST':
        form = StoryForm(request.POST, instance=story)
        if form.is_valid():
            story = form.save()
            return redirect('story_list')

    return render(request, 'story/edit.html', {'form': form})

def story_delete(request, id):
    story = get_object_or_404(Story, id=id)
    if request.method == 'POST':
        story.delete()

    return redirect('story_list')
