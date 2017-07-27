from django import forms

from .models import Track
from .models import Event
from .models import Story

class TrackForm(forms.ModelForm):

    class Meta:
        model = Track
        fields = '__all__'



class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('title', 'short_description', 'long_description', 'region')

        

class StoryForm(forms.ModelForm):

    class Meta:
        model = Story
        fields = '__all__'
