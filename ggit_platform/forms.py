from django import forms

from .models import Event
from .models import Member
from .models import Region
from .models import Story
from .models import Track


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = '__all__'
        widgets = {
            'icon': forms.DateInput(attrs={'placeholder':'Introdu link spre iconiță'}),
            'hero_image': forms.DateInput(attrs={'placeholder':'Introdu link spre imagine'}),

        }


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        widgets = {
            'photo': forms.DateInput(attrs={'placeholder':'Introdu link spre poză'}),
            'personal_page': forms.DateInput(attrs={'placeholder':'Introdu link spre poză'}),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'placeholder':'YYYY-MM-DD'}),
            'end_date': forms.DateInput(attrs={'placeholder':'YYYY-MM-DD'}),
            'application_start_date': forms.DateInput(attrs={'placeholder':'YYYY-MM-DD'}),
            'application_end_date': forms.DateInput(attrs={'placeholder':'YYYY-MM-DD'}),
            'thumbnail_image': forms.DateInput(attrs={'placeholder':'Introdu link spre poză'}),
            'hero_image': forms.DateInput(attrs={'placeholder':'Introdu link spre poză'}),

        }

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = '__all__'
        widgets = {
            'thumbnail_image': forms.DateInput(attrs={'placeholder':'Introdu link spre poză'}),
            'hero_image': forms.DateInput(attrs={'placeholder':'Introdu link spre poză'}),
        }


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = '__all__'
        widgets = {
            'thumbnail_image': forms.DateInput(attrs={'placeholder':'Introdu link spre poză'}),
            'hero_image': forms.DateInput(attrs={'placeholder':'Introdu link spre poză'}),
        }
