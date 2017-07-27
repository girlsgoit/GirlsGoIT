from django import forms

from .models import Track
from .models import Member 


class TrackForm(forms.ModelForm):

    class Meta:
        model = Track
        fields = '__all__'


class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = '__all__'
