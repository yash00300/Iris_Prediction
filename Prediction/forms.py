from .models import Data
from django import forms
    

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['sepalLengthCm', 'sepalWidthCm', 'petalLengthCm', 'petalWidthCm']
        widgets = {
            'sepalLengthCm': forms.NumberInput(attrs={'step': 0.1}),
            'sepalWidthCm': forms.NumberInput(attrs={'step': 0.1}),
            'petalLengthCm': forms.NumberInput(attrs={'step': 0.1}),
            'petalWidthCm': forms.NumberInput(attrs={'step': 0.1}),
        }