from django.shortcuts import render
from .models import Story
# Track views


# Region views


# Member views


# Event views


# Story views
def stories_list(request):
    stories = Story.objects.all()

    return render(request, 'story/list.html',{'stories': stories} )

def stories_detail(request, id):
    story = get_object_or_404(Story, id=id)
    
    return render(request, 'story/detail.html,' {'story':story})
