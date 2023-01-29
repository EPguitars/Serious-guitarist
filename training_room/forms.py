from django import forms
from .models import TrainingBlock

class BlockForm(forms.ModelForm):
    class Meta:
        model = TrainingBlock
        fields = ['name', 'duration']