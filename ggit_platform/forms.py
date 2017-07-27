from django import forms

from .models import Track
<<<<<<< HEAD
from .models import Member 

=======
from .models import Event
from .models import Story
>>>>>>> 27c0625fb74ac55b1e613fdaa8fe07aafcc276c8

class TrackForm(forms.ModelForm):

    class Meta:
        model = Track
        fields = '__all__'


<<<<<<< HEAD
class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
=======

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'

        

class StoryForm(forms.ModelForm):

    class Meta:
        model = Story
>>>>>>> 27c0625fb74ac55b1e613fdaa8fe07aafcc276c8
        fields = '__all__'
