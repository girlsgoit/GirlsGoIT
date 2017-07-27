from django import forms

from .models import Story


class StoryForm(forms.ModelForm):

    class Meta:
        model = Story
        fields = '__all__'
