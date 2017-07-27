from django import forms

from .models import Track
from .models import Event

class TrackForm(forms.ModelForm):

    class Meta:
        model = Track
        fields = '__all__'



class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'