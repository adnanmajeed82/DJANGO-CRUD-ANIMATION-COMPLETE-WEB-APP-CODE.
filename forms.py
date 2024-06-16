from django import forms
from .models import Animation

class AnimationForm(forms.ModelForm):
    class Meta:
        model = Animation
        fields = ['title', 'description', 'animation_file']
