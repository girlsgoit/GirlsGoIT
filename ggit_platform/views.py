from django.shortcuts import render
from .models import Member
from .models import Region
# Track views


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
