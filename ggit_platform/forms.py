from django import forms

from .models import Track
from .models import Event
from .models import Story
from .models import Region

class TrackForm(forms.ModelForm):

    class Meta:
        model = Track
        fields = '__all__'



class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'

        

class StoryForm(forms.ModelForm):

    class Meta:
        model = Story
        fields = '__all__'


class RegionForm(forms.ModelForm):

    class Meta:
        model = Region
        fields = '__all__'
