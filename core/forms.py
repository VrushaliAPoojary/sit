from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=("caption","image")
        
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'})
        }