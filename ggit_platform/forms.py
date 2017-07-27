from django import forms
from markdownx.fields import MarkdownxFormField

from .models import Track
from .models import Member 
from .models import Event
from .models import Story
from .models import Region

class TrackForm(forms.ModelForm):
    long_description = MarkdownxFormField()

    class Meta:
        model = Track
        fields = '__all__'


class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = '__all__'


class EventForm(forms.ModelForm):
    long_description = MarkdownxFormField()

    class Meta:
        model = Event
        fields = '__all__'

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = '__all__'

        


class StoryForm(forms.ModelForm):
    long_description = MarkdownxFormField()
    class Meta:
        model = Story
        fields = '__all__'


class RegionForm(forms.ModelForm):

    class Meta:
        model = Region
        fields = '__all__'
